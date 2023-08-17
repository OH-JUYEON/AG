from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignReview(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campagin__005/_T005.html')
