from django.shortcuts import render  # type: ignore
# from django.http import HttpResponse  # type: ignore

# Create your views here.
def home(request):
    
    context = {'text': 'Estou na HOME.'}
    
    return render(
        request,
        'home/index.html',
        context,
    )