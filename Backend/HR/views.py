 return JsonResponse({
        "Message":"Data not upload yet",
        "Status" : "Pending"
    })

    assessmentChoice = modal_data.get('assessmentChoice')
    questionType = modal_data.get('questionType')
    questionName = modal_data.get('questionName')
    questionMarks = modal_data.get('questionMarks')
    Answer = modal_data.get('Answer')
