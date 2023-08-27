from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignPhoto(View):

    def get(self, request, *args, **kwargs):



        return render(request, 'campaign/campaign-photo__001/_T006.html')
