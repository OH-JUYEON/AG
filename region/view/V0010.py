from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class SafetyScoreDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'region/region__002/_T002.html')
