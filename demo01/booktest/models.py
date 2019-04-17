from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField()
    #外键 第一个参数为表名 第二个参数代表删除类型
    hBook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

'''
Django MVT  M
ORM 对象中O 
需要定义实体类
'''