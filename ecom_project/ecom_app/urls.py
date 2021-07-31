
from django.urls import path
from ecom_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('single_product/<int:id>/', views.single_product, name='single_product'),
   
]
