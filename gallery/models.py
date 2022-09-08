from django.db import models


class Image(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "image"
