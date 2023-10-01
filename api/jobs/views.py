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
import spacy



class JobListingView(ListAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = JobListFilter



@api_view(["GET"])
def stats(request):
    jobs = JobListing.objects.all()
    roles = [
        ("Frontend","Frontend Engineer", "Frontend Developer"), 
        ("Backend","Backend Engineer", "Backend Developer"), 
        ("Product Manager","Product Developer", "Product Designer"), 
        ("Project Manager","Team Lead", "Senior Developer"), 
        ("Full Stack","Full-Stack", "Full stack Engineer", "Full Stack Developer"), 
        ("Designer","UI", "UI/UX", "Frontend Engineer"), 
    ]
    stat = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
    }

    nlp = spacy.load("en_core_web_sm")
    for job in jobs.iterator():
        _w = nlp(job.title)
        cur = []

        for role in roles:
            _temp_score = []
            for detail in role:
                _temp_score.append(_w.similarity(nlp(detail)))
            
            cur.append(max(_temp_score))

        _max = max(cur)
        idx = cur.index(_max)
        stat[idx] += 1

    _stat = {
        0 : "Frontend",
        1 : "Backend",
        2 : "Product Manager",
        3 : "Project Manager",
        4 : "Full Stack",
        5 : "Designer",
    }
    mapped = {}
    for key in stat.keys():
        mapped[_stat[key]] = stat[key]

    return Response(mapped, status=status.HTTP_200_OK)