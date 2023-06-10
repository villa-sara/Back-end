from rest_framework_nested import routers
from .views import LandOwnerViewSet

router = routers.DefaultRouter()
router.register('landowner', LandOwnerViewSet, 'landowner')
urlpatterns = [

]
urlpatterns.extend(router.urls)
