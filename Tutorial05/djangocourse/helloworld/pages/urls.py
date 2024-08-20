from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'), # ACTIVIDAD 1.
	path('products/', ProductIndexView.as_view(), name='index'), # Para ver ACTIVIDAD 2, ir a base.html y buscando la línea 27.
	path('products/create', ProductCreateView.as_view(), name='form'),
	path('products/<str:id>', ProductShowView.as_view(), name='show'),
]