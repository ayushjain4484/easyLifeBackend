from django.db import models


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=255)
    renews = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    frequency = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    logo = models.URLField(max_length=255)
    currency = models.CharField(max_length=255, default='EUR')

    def __str__(self):
        return self.service
