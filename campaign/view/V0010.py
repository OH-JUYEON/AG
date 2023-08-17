from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campagin__002/_T002.html')