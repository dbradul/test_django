import django_filters

from students.models import Student


class StudentFilter(django_filters.FilterSet):
    # email = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']