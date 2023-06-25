from django.urls import path
from . views import ContactAPIView

app_name = "core"

urlpatterns = [
    # ex: /api/
    # url(r'^$', views.index, name='index #Blackbox is wonderful
    path('contact/', view=ContactAPIView.as_view()),
    # path('', view='', context={}),
]
