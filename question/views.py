from django.shortcuts import render

# Create your views here.
from django.views import View


class QuestionView(View):
    def get(self, request):
        return render(request, 'question/question.html')

    def post(self, request):
        return render(request, 'question/questionok.html')

class QuestionokView(View):
    def get(self, request):
        return render(request, 'question/questionok.html')