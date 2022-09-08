from django.contrib.auth.models import User
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from users.serializers import CreateUserSerializer, RetrieveUserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RetrieveUserSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateUserSerializer
        return self.serializer_class
