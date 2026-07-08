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

class QuestionSetup(models.Model):
    # Question type for select question making type
    QUESTION_TYPE = (
        ('MCQ','Multiple Question'),
        ('SAQ','Short Question'),
    )
     # Answer selection
    ANSWER_CHOICE = (
        ('A','Option A'),
        ('B','Option B'),
        ('C','Option C'),
        ('D','Option D'),
    )
    questionId = models.AutoField(primary_key=True)
     # this part is connect the 'Assessment' table to 'QuestionSetup' table
    assessment = models.ForeignKey(Assessment,
                                   on_delete=models.CASCADE, 
                                   related_name="assessment_questions")
    
    questionType = models.CharField(max_length=50, choices=QUESTION_TYPE)
    questionName = models.TextField()
    marks = models.PositiveIntegerField(default=1)
    optionA = models.CharField(max_length=255, blank=True, null=True)
    optionB = models.CharField(max_length=255, blank=True, null=True)
    optionC = models.CharField(max_length=255, blank=True, null=True)
    optionD = models.CharField(max_length=255, blank=True, null=True)

     # This is for MCQ ANSWER set up
    correctAnswer = models.CharField(max_length=2,
                                     choices=ANSWER_CHOICE,
                                     blank=True,
                                     null=True)

    # This is for SAQ answer setup
    textAnswer = models.TextField(blank=True,null=True)
    
    class Meta:
        db_table = "assessment_questions"
        ordering = ["questionId"]

    def __str__(self):
        return f"{self.questionId} - {self.questionName[:50]}"
