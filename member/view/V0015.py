from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'AG/login/_T001.html')