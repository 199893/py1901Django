from django.db import models

# Create your models here.

class issueInfo(models.Model):
    isname=models.CharField(max_length=50)

    def __str__(self):
        return self.isname

class answerInfo(models.Model):
    awname=models.CharField(max_length=10)
    votes=models.CharField(max_length=100)
    isnameid=models.ForeignKey('issueInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.awname


