from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('movie_media/', include('movie_media.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('subscriber/', include('subscriber.urls')),
    path('about/', include('about.urls')),
    path('series/', include('series.urls')),
    path('contact/', include('contact.urls')),
    path('', home, name='home'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
