from django.urls import path
from jobs.views import JobListingView


urlpatterns = [
    path("jobs/", JobListingView.as_view(), name="job_listing")
]
