import json

from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from campaign.models import Campaign
from region.models import CityHeader


# Create your views here.
class CampaignMoreList(View):

    def get(self, request, *args, **kwargs):

        campaign_category = kwargs['category']
        city_headers = CityHeader.objects.all()

        if campaign_category == 'c':
            campaign_list = list(Campaign.objects.filter(campaign_category='캠페인').values("campaign_image.url", "campaign_description1", "campaign_description2", "campaign_description3"))
            campaign_category = '캠페인'

        campaigns = []
        for campaign in campaign_list:
            data = {'url': campaign.campaign_image.url, 'description1': campaign.campaign_description1,
                    'description2': campaign.campaign_description2, 'description3': campaign.campaign_description3}
            campaigns.append(data)

        context = {
        'campaigns': json.dumps(campaigns),
        'campaign_category': campaign_category,
        }

        return render(request, 'campaign/campaign-see-more/_T001.html', context)
