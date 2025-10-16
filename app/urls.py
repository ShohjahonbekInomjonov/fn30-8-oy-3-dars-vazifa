from django.urls import path
from .views import UserViewSet, CustomerViewSet, DeliveryViewSet, DishViewSet, DriverViewSet, MenuViewSet, OrderViewSet, PaymentViewSet, RestaurantViewSet, ReviewViewSet 

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('customers/', CustomerViewSet.as_view({'get': 'list'})),
    path('deliveries/', DeliveryViewSet.as_view({'get': 'list'})),
    path('dishes/', DishViewSet.as_view({'get': 'list'})),
    path('drivers/', DriverViewSet.as_view({'get': 'list'})),
    path('menus/', MenuViewSet.as_view({'get': 'list'})),
    path('orders/', OrderViewSet.as_view({'get': 'list'})),
    path('payments/', PaymentViewSet.as_view({'get': 'list'})),
    path('restaurans/', RestaurantViewSet.as_view({'get': 'list'})),
]