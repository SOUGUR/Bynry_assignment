from django.urls import path
from .views import view_pending_requests,resolve_request, logout_view
urlpatterns = [
    path('pending_requests/', view_pending_requests, name='view_pending_requests'),
    path('resolve-request/<int:request_id>/', resolve_request, name='resolve_request'), 
    path('logout/', logout_view, name='logout'), 
   
    ]