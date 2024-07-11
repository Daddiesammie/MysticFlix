from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = contact.subject
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\n{contact.message}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'contact/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
