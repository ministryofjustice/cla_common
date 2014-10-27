import datetime
import requests

from django import forms
from django.core.cache import cache
from django.utils.dateformat import format as date_format, time_format
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape, escape

from . import available, available_days, today_slots, tomorrow_slots
from .. import call_centre_availability


def day_choice(day):
    return (
        date_format(day, 'Ymd'),
        date_format(day, 'l jS'))


class AvailableDaysField(forms.ChoiceField):

    def __init__(self, num_days=6, *args, **kwargs):
        super(AvailableDaysField, self).__init__(*args, **kwargs)
        self.choices = map(day_choice, available_days(num_days))


def time_choice(time):
    return (
        time_format(time, 'Hi'),
        time_format(time, 'g:i A'))


class TimeSlotsSelect(forms.widgets.Select):

    def render_options(self, choices, selected_choices):
        self.choices = map(time_choice, self.choices_iterator())
        if len(self.choices) < 1:
            self.choices = [
                ('', {'label': 'No availability', 'disabled': True})]
        return super(TimeSlotsSelect, self).render_options(
            choices, selected_choices)

    def render_option(self, selected_choices, option_value, option_label):
        selected_html = ''
        if option_value in selected_choices:
            selected_html = u' selected="selected"'
        disabled_html = ''
        if hasattr(option_label, 'get'):
            if option_label.get('disabled'):
                disabled_html = u' disabled="disabled"'
            option_label = option_label.get('label', str(option_label))
        return (
            u'<option value="{value}"{selected}{disabled}>{label}'
            u'</option>').format(
                value=escape(option_value),
                selected=selected_html,
                disabled=disabled_html,
                label=conditional_escape(force_unicode(option_label)))


class TodaySlotsSelect(TimeSlotsSelect):
    choices_iterator = today_slots


class TomorrowSlotsSelect(TimeSlotsSelect):
    choices_iterator = tomorrow_slots
