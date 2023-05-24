from django.db import models
from django.utils import timezone


class Category(models.Model):
    db_table = "gallery_category"
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    db_table = "Images"
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    categories = models.ManyToManyField(Category, blank=True)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    @classmethod
    def images(cls):
        today = timezone.now().date()
        return cls.objects.filter(created_date__gte=today)

    @classmethod
    def get_image(cls, primary_key):
        return cls.objects.get(pk=primary_key)
