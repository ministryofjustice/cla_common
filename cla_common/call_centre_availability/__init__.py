import datetime
import requests

from django.core.cache import cache


BANK_HOLIDAYS_URL = 'https://www.gov.uk/bank-holidays/england-and-wales.json'


def current_datetime():
    # this function is to make unit testing simpler
    return datetime.datetime.now()


def in_the_past(time):
    return not time > current_datetime()


def before_9am(time):
    return not time.time() >= datetime.time(9, 0)


def after_8pm(time):
    return not time.time() < datetime.time(20, 0)


def on_sunday(time):
    return time.weekday() == 6


def parse_date(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d')


def get_date(bank_holiday):
    return parse_date(bank_holiday['date'])


def load_bank_holidays():
    holidays = requests.get(BANK_HOLIDAYS_URL).json()['events']
    return map(get_date, holidays)


def cache_bank_holidays(bank_holidays):
    one_year = 365 * 24 * 60 * 60
    cache.set('bank_holidays', bank_holidays, one_year)


def bank_holidays():
    bank_holidays = cache.get('bank_holidays')
    if not bank_holidays:
        bank_holidays = load_bank_holidays()
        cache_bank_holidays(bank_holidays)
    return bank_holidays


def on_bank_holiday(time):
    day = datetime.datetime.combine(time.date(), datetime.time())
    return day in bank_holidays()


def on_saturday(time):
    return time.weekday() == 5


def after_1230(time):
    return not time.time() < datetime.time(12, 30)


def is_today(time):
    return time.date() == current_datetime().date()


def too_late(time):
    one_hour = datetime.timedelta(minutes=60)
    now = current_datetime()
    return time.time() <= (now + one_hour).time()


def available(time):
    return not (
        in_the_past(time) or
        (before_9am(time) or after_8pm(time)) or
        on_sunday(time) or
        on_bank_holiday(time) or
        (on_saturday(time) and after_1230(time)) or
        (is_today(time) and too_late(time)))


def available_days(num):
    nine_am = datetime.time(9)
    today = datetime.datetime.combine(current_datetime().date(), nine_am)
    one_day = datetime.timedelta(days=1)
    while num:
        if available(today):
            value = date_format(today, 'Ymd')
            display = date_format(today, 'l jS')
            yield (value, display)
            num -= 1
        today = today + one_day


def every_interval(time, end, mins=15):
    interval = datetime.timedelta(minutes=mins)
    while time < end:
        yield time
        time += interval


def time_slots(day=None):
    if not day:
        day = datetime.date(1, 1, 1)  # Monday

    start = datetime.datetime.combine(day, datetime.time(9))
    end = datetime.datetime.combine(day, datetime.time(20))

    return list(filter(available, every_interval(start, end=end, mins=15)))


def today_slots(*args):
    return time_slots(current_datetime().date())


def tomorrow_slots(*args):
    tomorrow = current_datetime() + datetime.timedelta(days=1)
    return time_slots(tomorrow.date())


def time_choices(times):

    def time_choice(time):
        return (
            time_format(time, 'Hi'),
            time_format(time, 'g:i A'))

    return map(time_choice, times)
