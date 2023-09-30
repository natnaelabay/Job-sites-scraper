from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from jobs.serializers import JobListingSerializer
from jobs.models import JobListing
from jobs.filters import JobListFilter


class JobListingView(ListAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = JobListFilter
