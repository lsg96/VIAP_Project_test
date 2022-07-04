from django.shortcuts import render

# Create your views here.
from django.views import View


class Car_checkView(View):
    def get(self, request):
        return render(request, 'check/car_check.html')

    def post(self, request):
        pass


class Car_deliveryView(View):
    def get(self, request):
        return render(request, 'check/car_delivery.html')

    def post(self, request):
        pass


class Car_confirmView(View):
    def get(self, request):
        return render(request, 'check/car_confirm.html')

    def post(self, request):
        pass