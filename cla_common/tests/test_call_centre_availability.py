from datetime import datetime
import unittest
from contextlib import contextmanager

from .. import call_centre_availability
from ..call_centre_availability import available


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
