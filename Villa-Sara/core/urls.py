from rest_framework_nested import routers
from .views import UserViewSet, UserLoginView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()
router.register('users', UserViewSet, 'user-list')
urlpatterns = [
    path('users/hosts/', UserViewSet.as_view({'get': 'host_list'}), name='host-list'),
    path('users/hosts/<int:pk>/', UserViewSet.as_view({'get': 'host'}), name='host'),
    path('users/guests/', UserViewSet.as_view({'get': 'guest_list'}), name='guest-list'),
    path('users/guests/<int:pk>/', UserViewSet.as_view({'get': 'guest'}), name='guest'),
    path('users/login/', UserLoginView.as_view({'post': 'check_user'}), name='login'),
    path('users/register/', UserViewSet.as_view({'post': 'create_user'}), name='register'),
]
urlpatterns.extend(router.urls)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
