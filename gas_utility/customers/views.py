
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import SignUpForm
from .models import ServiceRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from .forms import CustomAuthenticationForm, ServiceRequestForm
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'customers/signup.html', {'form': form})

#login logic
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Using email for authentication
            if user is not None:
                login(request, user)
                if user.is_representative:
                    return redirect('view_pending_requests')  
                else:
                    return redirect('home')
            else:
                error_message = "Invalid credentials."
                return render(request, 'customers/login.html', {'form': form, 'error': error_message})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'customers/login.html', {'form': form})

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Set the customer to the logged-in user
            service_request.save()  # Save the instance to the database
            
            # Return a JSON response indicating success
            return JsonResponse({'success': True, 'message': 'Service request submitted successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ServiceRequestForm()

    return render(request, 'customers/home.html', {'form': form})

@login_required
def list_user_requests(request):
    # Get all service requests for the logged-in user
    user_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customers/user_requests.html', {'user_requests': user_requests})

@login_required
def user_profile(request):
    # The request.user object contains all the details of the logged-in user
    return render(request, 'customers/profile.html', {'user': request.user})