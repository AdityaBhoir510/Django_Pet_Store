from django.urls import path
from .views import place_order,payments,order_completed

app_name="orders"
urlpatterns = [
    path('billing/', place_order,name='place_order'),
    path('payment/', payments,name='payments'),
    path('orderplaced/', order_completed,name='orderplaced'),
]