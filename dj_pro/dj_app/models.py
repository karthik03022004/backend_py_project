from django.db import models

# Create your models here.
class Movies(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=20,unique=True)
    status=models.CharField(max_length=5)
    budget=models.IntegerField()
    pic=models.URLField()
