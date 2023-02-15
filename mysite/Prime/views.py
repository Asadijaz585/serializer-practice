from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # template = loader.get_template('D:/Projects/Scrap-Data/Current Work Space/Django/mysite/Prime/templates/prime/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    context = {'latest_question_list': latest_question_list} # render, instead of loader
    return render(request, 'D:/Projects/Scrap-Data/Current Work Space/Django/mysite/Prime/templates/prime/index.html', context)

def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'D:/Projects/Scrap-Data/Current Work Space/Django/mysite/Prime/templates/prime/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'D:/Projects/Scrap-Data/Current Work Space/Django/mysite/Prime/templates/prime/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)