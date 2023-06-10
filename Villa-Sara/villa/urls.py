from rest_framework_nested import routers
from .views import VillaViewSet
from django.urls import path
from django.contrib import admin
router = routers.DefaultRouter()
router.register('villa', VillaViewSet, 'villa')
urlpatterns = [

]
urlpatterns.extend(router.urls)
