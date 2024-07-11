# In core/context_processors.py

from .models import SiteConfiguration

def site_configuration(request):
    config = SiteConfiguration.objects.first()
    return {
        'site_config': config,
    }
