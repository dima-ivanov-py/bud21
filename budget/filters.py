from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import Balance, Profit, Expense


class BalanceFilter(FilterSet):
    class Meta:
        model = Balance
        fields = '__all__'
        exclude = ('user', 'total', 'pub_date')


class ProfitFilter(FilterSet):
    date_range = DateFromToRangeFilter(field_name='pub_date', widget=RangeWidget())
    class Meta:
        model = Profit
        fields = '__all__'
        exclude = ('user', 'pub_date')


class ExpenseFilter(FilterSet):
    date_range = DateFromToRangeFilter(field_name='pub_date', widget=RangeWidget())
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ('user', 'pub_date')
