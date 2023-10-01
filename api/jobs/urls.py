from django.urls import path
from jobs.views import JobListingView, role_stats, stack_stats 


urlpatterns = [
    path("jobs/", JobListingView.as_view(), name="job_listing"),
    path("jobs/role-stats/", role_stats, name="role_stats"),
    path("jobs/stack-stats/", stack_stats, name="stack_stats"),
]
