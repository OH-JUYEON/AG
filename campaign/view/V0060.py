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

        if campaign_category == 'j':
            campaigns = Campaign.objects.filter(campaign_category='지역순찰')
            campaign_category = '지역순찰'

        elif campaign_category == 'm':
            campaigns = Campaign.objects.filter(campaign_category='미화')
            campaign_category = '미화'

        elif campaign_category == 'b':
            campaigns = Campaign.objects.filter(campaign_category='봉사활동')
            campaign_category = '봉사활동'

        elif campaign_category == 'c':
            campaigns = Campaign.objects.filter(campaign_category='캠페인')
            campaign_category = '캠페인'

        context = {
            'campaigns': campaigns,
            'campaign_category': campaign_category,
        }

        # regions = []
        # for city_header in city_headers:
        #     regions.append({
        #         'city_name': city_header.city_name
        #     })
        #
        # context['regions'] = regions

        return render(request, 'campaign/campaign-see-more/_T001.html', context)
