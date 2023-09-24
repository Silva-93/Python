from django.urls import path  # type: ignore
from blog import views as blog_views

# HTTP request <-> HTTP response
# MVT (Model View Template)

app_blog = 'blog'

urlpatterns = [
    path('', blog_views.blog, name='blog'),  # Página HOME
    path('post/<int:id>', blog_views.post, name='post'),  # Página HOME
]
