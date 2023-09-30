from django.urls import path
from jobs.views import JobListingView, stats


urlpatterns = [
    path("jobs/", JobListingView.as_view(), name="job_listing"),
    path("jobs/stats/", stats, name="job_listing"),
]
