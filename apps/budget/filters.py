import django_filters

from .models import Balance, Profit, Expense


class BalanceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Balance
        fields = ("title",)


class ProfitFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr="icontains")
    date_range = django_filters.DateFromToRangeFilter(
        field_name="pub_date",
        widget=django_filters.widgets.RangeWidget(),
    )

    class Meta:
        model = Profit
        fields = ("balance", "title", "description", "total")


class ExpenseFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr="icontains")
    date_range = django_filters.DateFromToRangeFilter(
        field_name="pub_date",
        widget=django_filters.widgets.RangeWidget(),
    )

    class Meta:
        model = Expense
        fields = ("balance", "title", "description", "total")
