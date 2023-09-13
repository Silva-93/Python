# from django.shortcuts import render
from django.http import HttpResponse  # type: ignore

# Create your views here.
def home(request):
    return HttpResponse('HOME do APP')