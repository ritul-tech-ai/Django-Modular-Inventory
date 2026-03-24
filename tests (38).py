from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

# Views import karein
from vendor.views import VendorViewSet
from product.views import ProductViewSet
from course.views import CourseViewSet
from certification.views import CertificationViewSet
from vendor_product_mapping.views import VendorProductMappingViewSet

# Swagger Configuration
schema_view = get_schema_view(
   openapi.Info(
      title="Modular API System",
      default_version='v1',
      description="Internship Assignment APIs",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'products', ProductViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'vendor-product-mappings', VendorProductMappingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]