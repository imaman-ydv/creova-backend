from django.shortcuts import render, redirect
from .models import InterestSubmission

def home(request):
    return render(request, 'interest/index.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip.split(':')[0] if ip else None

def submit_interest(request):
    if request.method == 'POST':
        ip = get_client_ip(request)

        if InterestSubmission.objects.filter(ip_address=ip).exists():
            return render(request, 'interest/thank_you.html')

        InterestSubmission.objects.create(
            interest=request.POST.get('interest'),
            price=request.POST.get('price') or None,
            email=request.POST.get('email') or None,
            feedback=request.POST.get('feedback') or None,
            ip_address=ip,
        )
        return render(request, 'interest/thank_you.html')

    return redirect('/')
