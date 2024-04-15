import http

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("I am vicracker")


def new(request):
    return HttpResponse("New products")


new(http.HTTPMethod.GET)
index(http.HTTPMethod.GET)
