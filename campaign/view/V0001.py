from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignList(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campagin__001/_T001.html')