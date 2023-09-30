from django.db import models

# Create your models here.

class JobListing(models.Model):

    job_id = models.CharField(max_length=500)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=255)
    date = models.DateField()
    img = models.CharField(max_length=500)
    source = models.CharField(max_length=250)
    tags = models.JSONField(null=True)
    job_url = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, null=True)