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
def role_stats(request):
    jobs = JobListing.objects.all()[:30]
    roles = [
        ("Frontend", "Frontend Engineer", "Frontend Developer"),
        ("Backend", "Backend Engineer", "Backend Developer"),
        ("Product Manager", "Product Developer", "Product Designer"),
        ("Project Manager", "Team Lead", "Senior Developer"),
        ("Full Stack", "Full-Stack", "Full stack Engineer", "Full Stack Developer"),
        ("Designer", "UI", "UI/UX", "Frontend Engineer"),
    ]
    stat = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
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
        0: "Frontend",
        1: "Backend",
        2: "Product Manager",
        3: "Project Manager",
        4: "Full Stack",
        5: "Designer",
    }

    mapped = {}
    for key in stat.keys():
        mapped[_stat[key]] = stat[key]

    return Response(mapped, status=status.HTTP_200_OK)



@api_view(["GET"])
def stack_stats(request):
    jobs = JobListing.objects.all()[:30]
    roles = [
        ("React","React.js", "React Developer"), 
        ("Angular","Angular.js", "Angular Developer"), 
        ("Python","Python Developer", "Machine learning and AI", "Backend Engineer"), 
        ("Typescript","TypeScript Developer"), 
        ("Crypto","Web3", "blockchain", "Blockchain Developer"), 
        ("Node Js","express", "API", "Backend Engineer"), 
        ("Vue","Vue.js", "Vue Developer"), 
    ]
    stat = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
    }
    grouped_ds = {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : [],
        5 : [],
        6 : [],
    }

    nlp = spacy.load("en_core_web_sm")
    for job in jobs:
        _w = nlp(job.title)
        cur = []

        for role in roles:
            a = []
            for detail in role:
                a.append(_w.similarity(nlp(detail)))
            cur.append(max(a))

        _max = max(cur)
        idx = cur.index(_max)
        stat[idx] += 1
        # grouped_ds[idx].append(job)

    _stat = {
        0 : "React",
        1 : "Angular",
        2 : "Python",
        3 : "Typescript",
        4 : "Web 3",
        5 : "Node JS",
        6 : "Vue",
    }
    mapped = {}
    for key in stat.keys():
        mapped[_stat[key]] = stat[key]
        grouped_ds[_stat[key]] = grouped_ds[key]
        
    return Response(mapped, status=status.HTTP_200_OK)
