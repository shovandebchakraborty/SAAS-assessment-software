from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Dashboard(request):
    return render(request, 'assessment.html')

@csrf_exempt
def AssessmentCreate(request):
    modal_data = json.loads(request.body)
    
    if request.method != 'POST':
        return HttpResponse("<h2>Sorry! Its not POST method</h2>")
    else:
        examName = modal_data.get('examName')
        examTopic = modal_data.get('examTopic')
        examDuration = modal_data.get('examDuration')
        passingMarks = modal_data.get('passingMarks')
        startExam = modal_data.get('startExam')
        endExam =  modal_data.get('endExam')
        description = modal_data.get('description')
        instructions = modal_data.get('instructions')
        
        Assessment.objects.create(
            examName = examName,
            examTopic = examTopic,
            duration = examDuration,
            passingMarks = passingMarks,
            startTime = startExam,
            endTime = endExam,
            description = description,
            instruction = instructions
        )
        return JsonResponse({
            "status" : "Done",
            "Assessment" : examName,
            "Message" : "Assessment Upload succesfully"
        })