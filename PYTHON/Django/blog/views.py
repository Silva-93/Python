# from django.shortcuts import render
from django.http import HttpResponse  # type: ignore

# Create your views here.
def blog(request):
    return HttpResponse('BLOG do APP')