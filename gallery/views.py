from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gallery.models import Image
from gallery.serializers import CreateUpdateGallerySerializer, GallerySerializer


class GalleryViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH", "PUT"]:
            return CreateUpdateGallerySerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == "image_flush":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    @action(methods=["delete"], detail=False, url_path="image_flush")
    def image_flush(self, request):
        Image.objects.delete()
        return Response(status=204)
