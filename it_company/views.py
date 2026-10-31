
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Service, ContactRequest, Project
from .forms import ContactRequestForm


def home(request):
    services = Service.objects.filter(is_active=True)
    projects = Project.objects.filter(is_published=True)

    if request.method == 'POST':
        form = ContactRequestForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Thank you for contacting SCALLA. "
                "Your request has been received. "
                "We will get back to you shortly."
            )

            return redirect(reverse('home') + '#contact')

    else:
        form = ContactRequestForm()

    context = {
        'services': services,
        'projects': projects,
        'form': form,
    }

    return render(request, "it_company/home.html", context)


def privacy_policy(request):
    return render(request, "it_company/privacy_policy.html")
