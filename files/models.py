from django.db import models


class Alumni(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    degree = models.CharField(max_length=255)
    email = models.EmailField()
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.name
