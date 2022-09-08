from django.db import models

from gallery.managers import GalleryManager


class Image(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = GalleryManager()

    class Meta:
        db_table = "image"

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
