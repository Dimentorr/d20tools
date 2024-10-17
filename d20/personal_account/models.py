from django.db import models
from django.contrib.auth.models import User


class LogoAccount(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='personal_account/', default='')

    def __str__(self):
        return f'Logo from account {self.account} places - {self.logo}'

    class Meta:
        verbose_name = 'Аватарка'
        verbose_name_plural = 'Аватарки'
