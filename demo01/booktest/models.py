from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=100)
    #外键 第一个参数为表名 第二个参数代表删除类型
    hBook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

class AreaInfo(models.Model):
    atitle=models.CharField(max_length=20)
    aParent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.atitle



'''
Django MVT  M
ORM 对象中O 
需要定义实体类
'''