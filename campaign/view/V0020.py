from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignWrite(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campagin__003/_T003.html')
