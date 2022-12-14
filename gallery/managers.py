from django.db.models import Manager


class GalleryManager(Manager):
    def delete(self):
        for obj in self.get_queryset():
            obj.delete()
