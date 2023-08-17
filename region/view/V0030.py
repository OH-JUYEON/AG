from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class FundingInquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding/funding__004/_T004.html')

    def post(self, request, *args, **kwargs):
        return redirect('/funding/inquiry')
