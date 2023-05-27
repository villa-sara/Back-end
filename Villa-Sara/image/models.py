from django.db import models

class Image(models.Model):
    image = models.TextField(blank=True, verbose_name="تصویر")
