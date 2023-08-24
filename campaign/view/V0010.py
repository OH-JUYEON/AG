from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from campaign.models import Campaign
from member.models import Member
from region.models import CityHeader


# Create your views here.
class CampaignDetail(View):

    def get(self, request, *args, **kwargs):
        campaign_id = kwargs.get('campaign_id')

        campaign = get_object_or_404(Campaign, id=campaign_id)
        print(campaign.member_id)

        writer_instance = get_object_or_404(Member, id=campaign.member.id)
        region_instance = get_object_or_404(CityHeader, id=campaign.city_header.id)

        context = {
            'campaign': campaign,
            'writer': writer_instance.member_name,
            'region': region_instance.city_name
        }


        return render(request, 'campaign/campaign-detail__001/_T002.html', context)

