from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from  .views import ItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'item', viewset=ItemViewSet, basename='item')
router.register(r'order', viewset=OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]
