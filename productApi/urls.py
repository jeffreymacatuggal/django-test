from django.urls import include, path
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view 

schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version="1.0.0",
        description="API documentation for products"
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         include([
             path('', include(('api.urls', 'product'), namespace='products')),
             path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
         ]))
]