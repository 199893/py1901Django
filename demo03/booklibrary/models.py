from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Stunden(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    college=models.CharField(max_length=20)
    sno=models.IntegerField()
    eml=models.EmailField()
    state=models.BooleanField(default=False)


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
    statr=models.BooleanField(default=False)
    name=models.CharField(max_length=20,blank=True,null=True)


class HotPic(models.Model):
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='hotpic')
    index=models.SmallIntegerField(max_length=20)

    def __str__(self):
        return self.name

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hcontent=HTMLField()










