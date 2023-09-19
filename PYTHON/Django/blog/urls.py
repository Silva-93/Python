from django.urls import path  # type: ignore
from blog import views as blog_views

# HTTP request <-> HTTP response
# MVT (Model View Template)

urlpatterns = [
    path('', blog_views.blog, name='blog'),  # Página HOME
]
