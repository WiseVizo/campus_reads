from django.db import models
from students.models import CustomUser
from library.models import Book

# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

