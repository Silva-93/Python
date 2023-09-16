from django.urls import path  # type: ignore
from home import views as home_views

# HTTP request <-> HTTP response
# MVT (Model View Template)

urlpatterns = [
    path('', home_views.home),  # Página HOME
]
