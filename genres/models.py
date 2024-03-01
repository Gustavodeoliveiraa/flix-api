from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name
