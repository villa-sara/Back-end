from rest_framework_nested import routers
from .views import VillaViewSet, VillaMediaViewSet

router = routers.DefaultRouter()
router.register('contract', VillaViewSet, 'contract')
urlpatterns = [

]
urlpatterns.extend(router.urls)
