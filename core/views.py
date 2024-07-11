
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import SiteConfiguration

def site_configuration_view(request):
    config = get_object_or_404(SiteConfiguration)
    return render(request, 'home.html', {'site_config': config})


