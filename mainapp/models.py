from django.db import models

class Page(models.Model):
    name = models.CharField(unique=True, max_length=64)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='pages_images', blank=True)

    def __str__(self):
        return f"{self.name}"