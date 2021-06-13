from django.db import models

# Create your models here.
class Facts(models.Model):
    fact = models.TextField(default='Enter your facts here....')

class Category(models.Model):
    category = models.CharField(default='Enter Category', max_length=20)
