from datetime import datetime
import unittest
from contextlib import contextmanager

from django.forms import ValidationError
import django

from .. import call_centre_availability
from ..call_centre_availability import available, time_slots
from ..call_centre_availability.forms import AvailableDaysField, \
    TodaySlotsSelect


class MonkeyPatch(object):

    def __init__(self, obj, attr, value):
        self.obj = obj
        self.attr = attr
        self.applied = False

        if hasattr(obj, attr):
            self.original = getattr(obj, attr)
            setattr(obj, attr, value)
            self.applied = True

    def undo(self):
        if self.applied:
            setattr(self.obj, self.attr, self.original)


@contextmanager
def override_current_time(dt):
    override = lambda: dt
    patch = MonkeyPatch(call_centre_availability, 'current_datetime', override)
    yield
    patch.undo()


def mock_bank_holidays():
    return [datetime(2014, 12, 25, 0, 0)]


def pretty(time):
    return '{0:%a, %d %b %I:%M %p}'.format(time)


class CallCentreAvailabilityTestCase(unittest.TestCase):

    def setUp(self):
        self.bank_holiday_patch = MonkeyPatch(
            call_centre_availability,
            'bank_holidays',
            mock_bank_holidays)
        self.now = datetime(2014, 10, 22, 9, 0)

    def tearDown(self):
        self.bank_holiday_patch.undo()

    def assertAvailable(self, time):
        fail_msg = '{0} is not available at {1}'.format(
            pretty(time),
            pretty(self.now))
        with override_current_time(self.now):
            self.assertTrue(available(time), fail_msg)

    def assertNotAvailable(self, time):
        fail_msg = '{0} is available at {1}'.format(
            pretty(time),
            pretty(self.now))
        with override_current_time(self.now):
            self.assertFalse(available(time), fail_msg)

    def test_weekday_9am(self):
        self.assertAvailable(datetime(2014, 10, 23, 9, 0))

    def test_weekday_before_9am(self):
        self.assertNotAvailable(datetime(2014, 10, 23, 7, 0))

    def test_weekday_after_8pm(self):
        self.assertNotAvailable(datetime(2014, 10, 23, 21, 0))

    def test_saturday_after_1230pm(self):
        self.assertAvailable(datetime(2014, 10, 25, 12, 15))
        self.assertNotAvailable(datetime(2014, 10, 25, 12, 30))

    def test_sunday(self):
        self.assertNotAvailable(datetime(2014, 10, 26, 9, 0))

    def test_today_within_1hr(self):
        self.now = datetime(2014, 10, 23, 12, 0)
        self.assertNotAvailable(datetime(2014, 10, 23, 13, 0))
        self.assertAvailable(datetime(2014, 10, 23, 13, 15))

    def test_bank_holiday(self):
        self.assertNotAvailable(datetime(2014, 12, 25, 9, 0))

    def test_time_slots(self):
        with override_current_time(self.now):
            slots = time_slots(datetime(2014, 10, 23).date())
            self.assertEqual(slots[0], datetime(2014, 10, 23, 9, 0))
            map(lambda slot: self.assertTrue(available(slot)), slots)

    def test_no_availability(self):
        self.now = datetime(2014, 10, 25, 13, 0)
        with override_current_time(self.now):
            slots = time_slots(self.now.date())
            self.assertEqual(len(slots), 0)


class CallCentreAvailabilityFormsTestCase(django.test.TestCase):

    def setUp(self):
        self.bank_holiday_patch = MonkeyPatch(
            call_centre_availability,
            'bank_holidays',
            mock_bank_holidays)
        self.now = datetime(2014, 10, 22, 9, 0)

    def tearDown(self):
        self.bank_holiday_patch.undo()

    def test_available_days_field(self):
        with override_current_time(self.now):
            f = AvailableDaysField()
            self.assertEqual('20141022', f.clean('20141022'))
            self.assertEqual('20141023', f.clean('20141023'))
            self.assertEqual('20141024', f.clean('20141024'))
            self.assertEqual('20141025', f.clean('20141025'))
            self.assertRaises(ValidationError, f.clean, '20141026')
            self.assertEqual('20141027', f.clean('20141027'))
            self.assertEqual('20141028', f.clean('20141028'))
            self.assertRaises(ValidationError, f.clean, '20141029')

    def test_today_slots_select(self):
        with override_current_time(datetime(2014, 10, 25, 10, 30)):
            w = TodaySlotsSelect()
            self.assertHTMLEqual(
                w.render('time_today', '1215'),
                """<select name="time_today">
<option value="1145">11:45 AM</option>
<option value="1200">12:00 PM</option>
<option value="1215" selected="selected">12:15 PM</option>
</select>""")
