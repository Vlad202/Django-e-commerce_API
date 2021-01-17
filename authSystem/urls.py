from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('register/', views.UserCreate.as_view()),
    path('auth/', obtain_auth_token, name='api_token_auth'), 
]
