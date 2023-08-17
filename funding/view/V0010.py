from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class FundingDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding/funding__002/_T002.html')
