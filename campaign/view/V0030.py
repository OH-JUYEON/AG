from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class CampaignInquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campaign-inquiry__001/_T004.html')

    def post(self, request, *args, **kwargs):
        return redirect('/campaign/inquiry')
