import django_filters
from jobs.models import JobListing
from django.db.models import Q


class JobListFilter(django_filters.FilterSet):
    tags_contains = django_filters.CharFilter(method='filter_tags_contains')

    class Meta:
        model = JobListing
        fields = {
            "title": ["exact", "icontains"],
            "company": ["exact", "icontains"],
            "date": ["exact", "lt", "gt"],
            "source": ["exact", "icontains"],
            "location": ["exact", "icontains"],
        }

    def filter_tags_contains(self, queryset, name, value):
        if value.lower().__contains__("full"):
            value = "Full-time"

        return queryset.filter(Q(tags__contains=[value]))