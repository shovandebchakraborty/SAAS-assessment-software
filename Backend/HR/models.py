from django.db import models

# Create your models here.
class Assessment(models.Model):
    Id = models.AutoField(primary_key=True)
    examName = models.CharField(max_length=150, null=False)
    examTopic = models.CharField(max_length=100,null=False)
    