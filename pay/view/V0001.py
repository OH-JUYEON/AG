from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Pay(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'pay/pay__001/_T001.html')