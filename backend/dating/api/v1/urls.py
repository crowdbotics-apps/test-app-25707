from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    SettingViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    DislikeViewSet,
    InboxViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("userphoto", UserPhotoViewSet)
router.register("profile", ProfileViewSet)
router.register("inbox", InboxViewSet)
router.register("setting", SettingViewSet)
router.register("like", LikeViewSet)
router.register("match", MatchViewSet)
router.register("dislike", DislikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
