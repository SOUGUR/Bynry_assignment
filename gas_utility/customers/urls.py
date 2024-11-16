# urls.py
from django.urls import path
from .views import signup, login_view, create_service_request, list_user_requests, user_profile

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('request/', create_service_request, name='home'),
    path('my-requests/', list_user_requests, name='user_requests'), 
     path('profile/', user_profile, name='profile'),
]