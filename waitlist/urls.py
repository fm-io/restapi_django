# waitlist/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaitlistViewSet



router = DefaultRouter()
router.register(r'waitlist', WaitlistViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
