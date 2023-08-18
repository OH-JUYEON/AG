from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class SignUp(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'AG/signUp/_T001.html')