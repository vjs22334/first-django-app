from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    questions=Question.objects.order_by("-pub_date")[:5]
    context={ "question_list" : questions }
    return render(request,"polls/index.html",context)
    return HttpResponse("hello world, welcome to polls")
def details(request,question_id):
    try:
        question=Question.objects.get(id=question_id)
        context={ "question": question}
    except question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request,"polls/details.html",context)
def vote(request,question_id):
    return HttpResponse("you are voting on question %s" % question_id)
def results(request,question_id):
    return HttpResponse("you are viewing results of %s" % question_id)