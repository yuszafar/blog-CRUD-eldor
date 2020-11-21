from django.db import models


class Image(models.Model):
    saved_image = models.URLField()
