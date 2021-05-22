from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('manufacturer_register/',views.manufacturer_register.as_view(),name='manufacturer_register'),
    path('distributor_register/',views.distributor_register.as_view(),name='distributor_register'),
    path('retailer_register/',views.retailer_register.as_view(),name='retailer_register'),
    path('governmentbody_register/',views.governmentbody_register.as_view(),name='governmentbody_register'),
    path('normaluser_register/',views.normaluser_register.as_view(),name='normaluser_register'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_view,name='logout'),
]