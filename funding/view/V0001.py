from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class FundingDonationList(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding_donation/home/_T001.html')