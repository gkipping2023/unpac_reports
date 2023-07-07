from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/itinerarios', views.itinerarios, name='itinerarios'),
    path('/hoteles', views.hoteles, name='hoteles'),
    path('/empresa', views.empresa, name='empresa'),
    path('/transporte', views.transporte, name='transporte'),
]