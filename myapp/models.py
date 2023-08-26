from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)

    class Meta:
        db_table="user"