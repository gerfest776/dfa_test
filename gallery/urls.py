from rest_framework.routers import DefaultRouter

from gallery import views

gallery_router = DefaultRouter(trailing_slash=False)
gallery_router.register("gallery", views.GalleryViewSet)

urlpatterns = []
urlpatterns += gallery_router.urls
