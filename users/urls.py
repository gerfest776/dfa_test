from rest_framework.routers import DefaultRouter

from users import views

villager_router = DefaultRouter(trailing_slash=False)
villager_router.register("users", views.UserViewSet)

urlpatterns = []
urlpatterns += villager_router.urls
