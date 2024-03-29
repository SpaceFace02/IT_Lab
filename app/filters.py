from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （descending order）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='Name', lookup_expr='contains')
    memo = filters.CharFilter(label='Student Remarks', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': 'Name',
            'age': 'age',
        },
        label='Sort Order'
    )

    class Meta:
        model = Item
        fields = ('name', 'sex', 'memo',)
