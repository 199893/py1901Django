from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stunden(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    college=models.CharField(max_length=20)
    sno=models.IntegerField()
    eml=models.EmailField()


class Booktest(models.Model):
    bname=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publish=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    modified_time=models.DateTimeField(auto_now=True)
    state=models.BooleanField(default=False)


class Borrows(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    book_id=models.ForeignKey(Booktest,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)







