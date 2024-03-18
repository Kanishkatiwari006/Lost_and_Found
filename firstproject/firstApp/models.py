from django.db import models

# Create your models here.
class lost(models.Model):
    id=models.AutoField(primary_key=True)
    Product=models.CharField(max_length=50)
    Other=models.CharField(max_length=50)
    Address=models.CharField(max_length=1000)
    Pin=models.IntegerField()
    Ques=models.CharField(max_length=1000)
    Info=models.CharField(max_length=500)
    Num=models.IntegerField()
    Image=models.ImageField(upload_to='\files', default=None)


class found(models.Model):
    id=models.AutoField(primary_key=True)
    Product=models.CharField(max_length=50)
    Other=models.CharField(max_length=50)
    Address=models.CharField(max_length=1000)
    Pin=models.IntegerField()
    Email=models.EmailField(max_length=250)
    Ques=models.CharField(max_length=1000)

class contacts(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=250)
    Phone=models.IntegerField()
    Message=models.TextField(blank=False)