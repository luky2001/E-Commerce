from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('recipe/',views.recipe,name='recipe'),
    path('add/',views.add,name="'add"),
    path('update/<id>/',views.update,name='update'),
    path('delete/<id>/',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('vendor/',views.vendor,name='vendor'),
    path('update_details/',views.update_details,name='up'),
    path('vendor_details/',views.vendor_details,name='vendor_details')
]