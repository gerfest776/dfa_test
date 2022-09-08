from rest_framework.routers import DefaultRouter

from users import views

user_router = DefaultRouter(trailing_slash=False)
user_router.register("users", views.UserViewSet)

urlpatterns = []
urlpatterns += user_router.urls
