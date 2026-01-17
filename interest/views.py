from django.shortcuts import render, redirect
from .models import InterestSubmission


def home(request):
    return render(request, "interest/index.html")


def submit_interest(request):
    if request.method == "POST":
        ip_address = get_client_ip(request)

        # 🔒 Check: 1 IP = 1 submit
        if InterestSubmission.objects.filter(ip_address=ip_address).exists():
            # Duplicate submit → silently ignore
            return render(request, "interest/thank_you.html")

        interest = request.POST.get("interest")
        price = request.POST.get("price") or None
        email = request.POST.get("email") or None
        feedback = request.POST.get("feedback") or None

        InterestSubmission.objects.create(
            interest=interest,
            price=price,
            email=email,
            feedback=feedback,
            ip_address=ip_address,
        )

        return render(request, "interest/thank_you.html")

    return redirect("/")


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
