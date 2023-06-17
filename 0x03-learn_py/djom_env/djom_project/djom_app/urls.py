from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import LoginForm

'''
ADVISORY

do not use the following imports in production.
repeat: do not use the following imports in production
'''
from django.conf import settings
from django.conf.urls.static import static

app_name = 'djom_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm),
        name='login'),
    # path(''),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
