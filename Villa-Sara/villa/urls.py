from rest_framework_nested import routers
from .views import VillaViewSet, VillaMediaViewSet

router = routers.DefaultRouter()
router.register('villa', VillaViewSet, 'villa')
router.register('villamedia', VillaMediaViewSet, 'villamedia')
urlpatterns = [

]
urlpatterns.extend(router.urls)
