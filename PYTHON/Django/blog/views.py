from django.shortcuts import render  # type: ignore
# from django.http import HttpResponse  # type: ignore

# Create your views here.
def blog(request):
    return render(
        request,
        'blog/index.html'
    )