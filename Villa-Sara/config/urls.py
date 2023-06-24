from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_nested import routers
from villa.urls import router as villa_router
from tenant.urls import router as tenant_router
from landowner.urls import router as landowner_router
from contract.urls import router as contract_router

router = routers.DefaultRouter()
router.registry.extend(villa_router.registry)
router.registry.extend(tenant_router.registry)
router.registry.extend(landowner_router.registry)
router.registry.extend(contract_router.registry)

swagger_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger', swagger_view),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)