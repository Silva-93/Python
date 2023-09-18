from django.shortcuts import render  # type: ignore
# from django.http import HttpResponse  # type: ignore

# Create your views here.
def blog(request):
    
    context = {'text': 'Estou no BLOG!'}
    
    return render(
        request,
        'blog/index.html',
        context,
    )