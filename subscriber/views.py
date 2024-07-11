# subscriber/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm # type: ignore

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')  # Change 'home' to your homepage URL name
    else:
        form = SubscriberForm()
    return render(request, 'subscriber/subscribe.html', {'form': form})
