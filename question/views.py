from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from question.models import Question


class QuestionView(View):
    def get(self, request):
        return render(request, 'question/question.html')

    def post(self, request):
        form = request.POST.dict()

        q = Question(qname=form['qname'], qphone=form['qphone'],
                     qemail=form['qemail'], qselect=form['qselect'],
                     qsubject=form['qsubject'], context=form['qtext'])
        q.save()

        return redirect('/question/questionok?qname=' + form['qname'])

class QuestionokView(View):
    def get(self, request):
        form = request.GET.dict()

        q = Question.objects.select_related().get(qname=form['qname'])

        context = {'q': q}
        return render(request, 'question/questionok.html', context)


