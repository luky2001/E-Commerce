from django.urls import path
from . import views

urlpatterns = [
    path('', views.homes, name = 'homes'),
    path('customer_register/',views.customer_register,name="customer_register"),
    path('customer_login/',views.customer_login,name="customer_login"),
    path('customer_logout/',views.customer_logout,name="customer_logout"),
    path('customer_profile/',views.customer_profile,name="customer_profile"),
    path('customer_details/',views.customer_details,name="customer_details"),
    path('customer_update/',views.customer_update,name="customer_update"),
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),
    path('cart/',views.cart,name='cart'),
    path('addcart/<int:product_id>/',views.addcart,name='addcart'),
    path('remove_cart/<id>/',views.remove_cart,name='remove_cart'),
 ]