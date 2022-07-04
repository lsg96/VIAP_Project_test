from django.shortcuts import render
from django.views import View

# Create your views here.


class FaqView(View):
    def get(self, request):
        return render(request, 'community/faq.html')

    def post(self, request):
        pass


class InfoView(View):
    def get(self, request):
        return render(request, 'community/information.html')

    def post(self, request):
        pass


class ReviewView(View):
    def get(self, request):
        return render(request, 'community/review.html')

    def post(self, request):
        pass