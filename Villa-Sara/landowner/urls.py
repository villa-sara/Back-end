from rest_framework_nested import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
urlpatterns = [

]

urlpatterns.extend(router.urls)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
