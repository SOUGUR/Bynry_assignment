from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from customers.models import ServiceRequest
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.utils import timezone 




@login_required  # Ensure the user is logged in
def view_pending_requests(request):
    if not request.user.is_representative:
        return redirect('home') 

    # Retrieve all pending service requests
    pending_requests = ServiceRequest.objects.filter(status='Pending')

    return render(request, 'representatives/pending_requests.html', {'pending_requests': pending_requests})

@login_required
def resolve_request(request, request_id):
    if request.method == "POST":
        if not request.user.is_representative:
            return JsonResponse({'error': 'Unauthorized access'}, status=403)  # Restrict access

        service_request = get_object_or_404(ServiceRequest, id=request_id)

        # Update the status to 'Resolved'
        service_request.status = 'Resolved'
        service_request.resolved_on = timezone.now()
        service_request.save()

        return JsonResponse({'success': True})  

    return JsonResponse({'error': 'Invalid request'}, status=400)

# Log out the user
def logout_view(request):
    logout(request)  
    return redirect('login') 
