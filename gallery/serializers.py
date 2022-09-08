from rest_framework import serializers

from gallery.models import Image


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "image", "created_at")


class CreateUpdateGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)
