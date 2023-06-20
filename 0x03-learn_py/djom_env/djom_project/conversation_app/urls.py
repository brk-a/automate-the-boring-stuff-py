from django.urls import path
from . import views

app_name = 'conversation_app'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new_conversation'),
    # path('', views.new_item, name='new_item'),
    # path(''),
]

# 'new/<int:item_pk>/'
# 'new/<int:item_pk>'