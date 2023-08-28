from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding
from donation.models import Donation
from campaign.models import Campaign
from django.db.models import Count, F


# Create your views here.
class Search(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        campaign = Campaign.objects.annotate(campaign_participant_count=Count('campaignparticipant__campaign_id')).filter(campaign_content__icontains=query,status=1).order_by('-id')
        funding = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(funding_content__icontains=query,status=1).order_by('-id')
        donation = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(donation_content__icontains=query,status=1).order_by('-id')
        return render(request, 'funding_donation/search/_T001.html',{'campaign':campaign,'len1':campaign.count(), 'funding':funding,'len2':funding.count(),'donation':donation,'len3':donation.count()})
