from django.urls import path
from .views import cart_home,update_cart,add_to_cart,delete_cart

app_name="cart"
urlpatterns = [
    path('cartpage/', cart_home, name='cartpage'),
    path('updatecart/', update_cart, name='updatecart'),
    path('updatecart/<int:id>', add_to_cart, name='addtocart'),
    path('deleteitem/<int:id>', delete_cart, name='deleteitem'),
]
