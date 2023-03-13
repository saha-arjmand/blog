from django.shortcuts import render
from question.models import Question

def question_view(request):

    context = {}
    # context['some_string'] = "this is some string that I'm passing to the view"
    # context['some_number'] = 123456

    # context = {
    #         'some_string' : "this is some string that I'm passing to the view",
    #         'some_number' : 123456,
    # }

    # list_of_values = []
    # list_of_values.append("first entry")
    # list_of_values.append("second entry")
    # list_of_values.append("third entry")
    # list_of_values.append("forth entry")
    # context['list_of_values'] = list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, "question/home.html", context)