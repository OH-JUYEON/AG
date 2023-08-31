from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
class CampaignInquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campaign-inquiry__001/_T004.html')

    def post(self, request, *args, **kwargs):
        print('11111111111')
        try:
            data = json.loads(request.body)
            type = ''


            print(data['name'])
            location = CityDetail.objects.filter(city_detail_name=data['name'])
            category = Campaign.objects.filter(campaign_category=type, city_detail_id=location[0].id)
            city = location[0].city_detail_name

            queryset_json = serializers.serialize('json', category)
            print(queryset_json)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        return JsonResponse({'result': queryset_json, 'city': city}, status=200)
