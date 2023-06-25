"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.registry.extend(villa_router.registry)
router.registry.extend(tenant_router.registry)
router.registry.extend(landowner_router.registry)
router.registry.extend(contract_router.registry)

swagger_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', swagger_view),
    # path('auth/', include('rest_framework.urls')),
    # path('auth-token/', views.obtain_auth_token),
    # path('auth/', include("dj_rest_auth.urls")),
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('', include(('core.urls', 'core'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
