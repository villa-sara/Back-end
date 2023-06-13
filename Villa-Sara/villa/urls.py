from rest_framework_nested import routers
from .views import VillaViewSet, VillaMediaViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('villa', VillaViewSet, 'villa')
router.register('villamedia', VillaMediaViewSet, 'villamedia')
router.register('rentalperiod', VillaViewSet, 'rentalperiod')
urlpatterns = [

]
urlpatterns.extend(router.urls)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)