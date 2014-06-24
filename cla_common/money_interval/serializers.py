from rest_framework.serializers import WritableField

from .models import MoneyInterval
from .fields import MoneyIntervalField


class MoneyIntervalDRFField(WritableField):
    type_name = 'MoneyIntervalDRFField'
    type_label = 'moneyIntervalDRFField'
    form_field_class = MoneyIntervalField

    def field_to_native(self, obj, field_name):

        moneyIntervalField = getattr(obj, field_name)
        return {
            'interval_period' : moneyIntervalField.interval_period,
            'per_interval_value' : moneyIntervalField.per_interval_value,
        }

    def from_native(self, value):
        # TODO remove word earnings and find it as field
        if isinstance(value, dict):
            mi = MoneyInterval(
                value['interval_period'], pennies=value['per_interval_value']
            )
        else:
            # TODO - remove - only here for mock test - temporary
            mi = MoneyInterval('per_month', pennies=value)
        return mi


class MoneyIntervalModelSerializerMixin(object):
    def __init__(self, *args, **kwargs):
        # add a model serializer which is used throughout this project
        self.field_mapping = self.field_mapping.copy() # ouch
        self.field_mapping[MoneyIntervalField] = MoneyIntervalDRFField
        super(MoneyIntervalModelSerializerMixin, self).__init__(*args, **kwargs)
