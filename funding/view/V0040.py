from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding
from donation.models import Donation
from campaign.models import Campaign


# Create your views here.
class Search(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        campaign = Funding.objects.filter(funding_content__icontains=query)
        funding = Campaign.objects.filter(campaign_content__icontains=query)
        donation = Donation.objects.filter(donation_content__icontains=query)

        return render(request, 'funding_donation/search/_T001.html',{'campaign':campaign,'funding':funding,'donation':donation})
