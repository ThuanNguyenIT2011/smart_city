from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),   # <-- login
    path('', views.api_home_view, name='api_home'),
    path('config/', include('config.urls')),
]
