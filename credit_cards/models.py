from django.db import models


class CreditCard(models.Model):
    name = models.CharField(max_length=60)
    pan = models.CharField(max_length=20)

    def __str__(self):
        return self.name
