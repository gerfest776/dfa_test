from rest_framework.viewsets import ModelViewSet

from gallery.models import Image
from gallery.serializers import CreateUpdateGallerySerializer, GallerySerializer


class GalleryViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = GallerySerializer

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH", "PUT"]:
            return CreateUpdateGallerySerializer
        return self.serializer_class
