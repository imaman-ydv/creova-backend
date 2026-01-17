from django.shortcuts import render, redirect
from .models import InterestSubmission


def home(request):
    return render(request, "interest/index.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        # client ka real IP (first one)
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    # 🔥 port remove karo (106.205.x.x:30125 → 106.205.x.x)
    if ip and ":" in ip:
        ip = ip.split(":")[0]

    return ip


def submit_interest(request):
    if request.method == "POST":
        ip_address = get_client_ip(request)

        # 🔒 1 IP = 1 submit
        if InterestSubmission.objects.filter(ip_address=ip_address).exists():
            return render(request, "interest/thank_you.html")

        InterestSubmission.objects.create(
            interest=request.POST.get("interest"),
            price=request.POST.get("price") or None,
            email=request.POST.get("email") or None,
            feedback=request.POST.get("feedback") or None,
            ip_address=ip_address,
        )

        return render(request, "interest/thank_you.html")

    return redirect("/")
