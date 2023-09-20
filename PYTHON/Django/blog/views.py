from django.shortcuts import render  # type: ignore
from blog.data import posts

# Create your views here.
def blog(request):
    
    context = {
        'text': 'Estou no BLOG!',
        'posts': posts
        }
    
    return render(
        request,
        'blog/index.html',
        context,
    )