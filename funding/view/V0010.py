from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding
from django.db.models import Count, F
from campaign.models import CampaignReview


# Create your views here.
class FundingDetail(View):

    def get(self, request, *args, **kwargs):
        funding = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(id=kwargs['funding_header_id'],status=1)[0]
        reviews = CampaignReview.objects.filter(campaign=funding.campaign_id).count() 
        return render(request, 'funding_donation/funding__001/_T001.html',{'funding':funding,'reviews':reviews})
