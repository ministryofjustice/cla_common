from decimal import Decimal

from django.utils.translation import ugettext_lazy as _

TWO_DP = Decimal('.01')
ZERO_DP = Decimal('1')

class MoneyInterval(object):
    value = None # in pennies
    interval_period = None
    per_interval_value = None  # in pennies

    #            interval_name, user_copy_name, multiply_factor (to get monthly value)
    _intervals = [('per_week', _('Per Week'), 52.0/12.0),
                  ('per_4week', _('4 Weekly'), 13.0/12.0),
                  ('per_month', _('Per Month'), 1.0),
                  ('per_year', _('Per Year'), 1.0/12.0)
                 ]

    _intervals_dict = {i[0]: {'user_copy_name': i[1], 'multiply_factor': i[2]} for i in _intervals}

    def __init__(self, interval_period, pennies=None, pounds=None):
        
        if interval_period not in self._intervals_dict.keys():
            raise ValueError("Invalid interval period")
        
        if (pennies==None and pounds==None) or (pennies!=None and pounds!=None):
            raise ValueError("Amount needs to be set")

        self.interval_period = interval_period

        if pennies!=None:
            self._set_as_pennies(pennies)
        else:
            self._set_as_pennies(int(Decimal(pounds).quantize(ZERO_DP))*100)


    def is_valid_interval_period(self, interval_period):
        return interval_period in self._intervals_dict

    def _set_as_pennies(self, per_interval_value=None):
        self.per_interval_value = per_interval_value
        multiply_factor = self._intervals_dict[self.interval_period]['multiply_factor']
        self.value = multiply_factor * self.per_interval_value

    @staticmethod
    def get_intervals_for_widget():
        """
        @return: list of tuples for dropdown widget
        """
        return [(i[0], i[1]) for i in MoneyInterval._intervals]
    
    def as_monthly(self):
        """
        @param interval_value: Decimal
        @param interval_name: enum from MoneyInterval._intervals
        @return: float
        """
        multiply_factor = float(MoneyInterval._intervals_dict[self.interval_period]['multiply_factor'])
        per_month = float(self.per_interval_value) * multiply_factor
        return int(per_month)

    def as_dict(self):
        return {    'interval_period' : self.interval_period,
                    'per_interval_value' : self.per_interval_value
                }
