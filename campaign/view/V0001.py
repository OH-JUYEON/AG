from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from campaign.models import Campaign
from region.models import CityHeader


# Create your views here.
class CampaignList(View):

    def get(self, request, *args, **kwargs):

        campaigns = Campaign.objects.filter(campaign_category='지역순찰')\
                        .annotate(member_count=Count('member')) \
                        .order_by('-member_count')[:4][:4]
        city_headers = CityHeader.objects.all()

        context = {
            'campaigns': campaigns
        }

        regions = []
        for city_header in city_headers:
            regions.append({
                'city_name': city_header.city_name
            })

        context['regions'] = regions

        return render(request, 'campaign/campaign__001/_T001.html', context)
