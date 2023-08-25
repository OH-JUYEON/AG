from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class FundingDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding_donation/funding__001/_T001.html')
