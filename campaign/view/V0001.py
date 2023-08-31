from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from campaign.models import Campaign
from campaign.view.serializers import CampaignSerializer
from region.models import CityHeader, CityDetail
import json
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
class CampaignList(View):
    def get(self, request, *args, **kwargs):
        print('들어옴')
        return render(request, 'campaign/campaign__001/_T001.html')


class CampaignListAPI(APIView):

    def get(self, request):
        city_headers = CityHeader.objects.all()
        regions = []
        all_campaigns = []
        result = {}
        for city_header in city_headers:
            regions.append({
                'city_name': city_header.city_name
            })

            campaign_list = Campaign.objects.filter(city_header_id=CityHeader.objects.get(city_name=city_header.city_name).id).order_by('id')[:4]
            campaigns = []
            for campaign in campaign_list:
                data = {'title': campaign.campaign_title, 'url': campaign.campaign_image.url, 'description1': campaign.campaign_description1,
                        'description2': campaign.campaign_description2, 'description3': campaign.campaign_description3, 'id':campaign.id}
                campaigns.append(data)
            if campaigns:
                all_campaigns.append(campaigns)

        result['regions'] = regions
        result['all_campaigns'] = all_campaigns

        return Response(result)

    def post(self, request):
        categories = ['지역순찰', '미화', '봉사활동', '캠페인']
        try:
            data = json.loads(request.body)
            filtered_campaigns = Campaign.objects.all()

            if data.get('type') == 0:
                filtered_campaigns = filtered_campaigns.filter(campaign_category=categories[data['type']])  
            elif data.get('type'):
                filtered_campaigns = filtered_campaigns.filter(campaign_category=categories[data['type']])

  

            if data['name'] != "지역선택":
                location = CityDetail.objects.get(city_detail_name=data['name'])
                filtered_campaigns = filtered_campaigns.filter(city_detail_id=location.id)

        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON'})

        return Response(CampaignSerializer(filtered_campaigns, many=True).data)
