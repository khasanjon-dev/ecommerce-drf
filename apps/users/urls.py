from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshSlidingView, TokenObtainPairView

from users.views import UserModelViewSet

router = DefaultRouter()
router.register('', UserModelViewSet, 'users')

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshSlidingView.as_view(), name='refresh'),
    path('', include(router.urls)),
]
