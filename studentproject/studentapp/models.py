from django.db import models


# Create your models here.
class studentinfo(models.Model):
    roll_number=models.IntegerField(primary_key=True)
    fullname=models.CharField(max_length=25)
    date_of_birth=models.DateField()
    email=models.CharField(max_length=30)


