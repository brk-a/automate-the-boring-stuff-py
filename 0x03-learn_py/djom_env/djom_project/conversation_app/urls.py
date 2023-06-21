from django.urls import path
from . import views

app_name = 'conversation_app'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new_conversation'),
    path('', views.inbox, name='inbox'),
    # path(''),
]
