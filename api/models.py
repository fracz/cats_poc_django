from django.db import models


class Cat(models.Model):
    url = models.CharField(max_length=1024)
    creator = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} by @{1}'.format(self.url, self.creator)
