from django.db import models

# Create your models here.
class News(models.Model):
    fact = models.TextField(default = 'Enter your facts here....')