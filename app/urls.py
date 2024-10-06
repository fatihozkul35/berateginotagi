from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
   path('', views.home, name="home"),
   path('events', views.events, name="events"),
   path('about', views.about, name="about"),
   path('contact', views.contact, name="contact"),
   path('test', views.test, name="test"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
