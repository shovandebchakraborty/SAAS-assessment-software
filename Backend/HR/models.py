from django.db import models

# Create your models here.
class Assessment(models.Model):
    Id = models.AutoField(primary_key=True)
    examName = models.CharField(max_length=150)
    examTopic = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )
    passingMarks = models.PositiveIntegerField(default=60)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    description = models.TextField()
    instruction = models.TextField()

    def __str__(self):
        return f"{self.examName} | {self.examTopic} | {self.duration} Minutes"