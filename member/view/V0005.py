from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Main(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'AG/main/_T001.html')