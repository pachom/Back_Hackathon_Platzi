"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'users/musiclistsinprofile/', user_views.MusicListInProfileViewSet, basename='musiclistinprofile')

urlpatterns = [
    path('', include(router.urls))
]
