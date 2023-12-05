from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('itinerarios', views.itinerarios, name='itinerarios'),
    path('hoteles', views.hoteles, name='hoteles'),
    path('empresa', views.empresa, name='empresa'),
    path('entrenamiento', views.entrenamiento, name='entrenamiento'),
    path('seg_op', views.seg_op, name='seg_op'),
    path('sal_oc', views.sal_oc, name='sal_oc'),
]