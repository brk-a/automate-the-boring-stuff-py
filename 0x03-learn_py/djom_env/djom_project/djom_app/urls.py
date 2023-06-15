from django.urls import path
from . import views
'''
ADVISORY

do not use the following imports in production.
repeat: do not use the following imports in production
'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    # path(''),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
