from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
def Dashboard(request):
    return render(request, 'assessment.html')

def AssessmentCreate(request):
    modal_data = json.load(request.body)
    
    if request.method != 'POST':
        return HttpResponse("<h2>Sorry! Its not POST method")
    else:
        examName = modal_data.get('examName')
        examTopic = modal_data.get('examTopic')
        examDuration = modal_data.get('examDuration')
        passingMarks = modal_data.get('passingMarks')
        startExam = modal_data.get('startExam')
        endExam =  modal_data.get('endExam')
        description = modal_data.get('description')
        instructions = modal_data.get('instructions')
        