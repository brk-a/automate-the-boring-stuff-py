from django.urls import path
from . import views

app_name = 'item_app'

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    # path(''),
]