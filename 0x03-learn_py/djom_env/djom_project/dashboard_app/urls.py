from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new_item, name='new_item'),
    # path(''),
]