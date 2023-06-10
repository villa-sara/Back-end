from .views import TenantViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('Tenant', TenantViewSet, 'tenant')

urlpatterns = [

]
urlpatterns.extend(router.urls)
