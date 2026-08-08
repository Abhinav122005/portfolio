from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

# Home Page View
def index(request):
    return render(request, 'portfolio_app/index.html', {'is_home_page': True})

# About Page View
def about(request):
    return render(request, 'portfolio_app/about.html')

# Internships Page View
def internships(request):
    return render(request, 'portfolio_app/internships.html')

# Services Page View
def services(request):
    return render(request, 'portfolio_app/services.html')

# Skills Page View
def skills(request):
    return render(request, 'portfolio_app/skills.html')

# Projects Page View
def projects(request):
    return render(request, 'portfolio_app/projects.html', {'is_home_page': False})

# Contact Page View (Handles GET and form POST)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send Email Notification
            try:
                email_subject = f"New Portfolio Message from {name}: {subject}"
                email_message = f"You have received a new message from your portfolio website.\n\nName: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
                send_mail(
                    email_subject,
                    email_message,
                    settings.EMAIL_HOST_USER, # From email (your authenticated email)
                    [settings.EMAIL_HOST_USER], # To email (send to yourself)
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                # If email fails (e.g. invalid credentials), still let user know it was saved
                print(f"Email failed to send: {e}")
                messages.warning(request, 'Your message was saved, but the email notification failed to send. Check server logs.')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please fill out all required fields.')

    return render(request, 'portfolio_app/contact.html')
