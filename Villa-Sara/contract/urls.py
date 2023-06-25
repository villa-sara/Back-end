from rest_framework_nested import routers
from .views import ContractViewSet

router = routers.DefaultRouter()
router.register('contract', ContractViewSet, 'contract')
urlpatterns = [

]
urlpatterns.extend(router.urls)
