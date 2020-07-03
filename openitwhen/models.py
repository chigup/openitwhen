from django.db import models


class Letters(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title