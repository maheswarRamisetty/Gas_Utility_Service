from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def submit_request(request):
    submission_success=False
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  
        if form.is_valid():  
            service_request = form.save(commit=False)  
            service_request.user = request.user.username 
            service_request.save()  
            submission_success=True
            return redirect('home') 
    else:
        form = ServiceRequestForm()  
    return render(request, 'submit_request.html', {'form': form}) 

@login_required
def track_request(request):
    service_requests = ServiceRequest.objects.filter(user=request.user)  
    return render(request, 'track_request.html', {'service_requests': service_requests})
def home(request):
    return render(request, 'Home_Service.html')