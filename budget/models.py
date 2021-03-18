from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=21)
    total = models.DecimalField(max_digits=13, decimal_places=2)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Profit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=21, default='', blank=True)
    title = models.CharField(max_length=21)
    description = models.CharField(max_length=50, default='', blank=True)
    total = models.DecimalField(max_digits=13, decimal_places=2)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=21, default='', blank=True)
    title = models.CharField(max_length=21)
    description = models.CharField(max_length=50, default='', blank=True)
    total = models.DecimalField(max_digits=13, decimal_places=2)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
