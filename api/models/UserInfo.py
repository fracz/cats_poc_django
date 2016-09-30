from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_ip = models.GenericIPAddressField(verbose_name='Last login IP', protocol='IPv4')

    def __str__(self):
        return 'IP: ' + self.last_ip
