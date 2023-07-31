from django.urls import include, path
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]