from rest_framework.serializers import ModelSerializer
from jobs.models import JobListing


class JobListingSerializer(ModelSerializer):
    class Meta:
        model = JobListing
        fields = "__all__"
