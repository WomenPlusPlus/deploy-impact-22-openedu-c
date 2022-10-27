from django.db import models

# Create your models here.
class Category(models.Model):
     category_id = models.IntegerField()
     category_name = models.CharField(max_length=30)


