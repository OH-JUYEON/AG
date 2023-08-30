from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding
from donation.models import Donation
from campaign.models import Campaign
from django.db.models import Count, F
from region.models import CityDetail
import json
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
class FundingDonationList(View):

    def get(self, request, *args, **kwargs):
        kwargs['region'] ='강동구'
        if kwargs['region'] != 'all':
            city = CityDetail.objects.filter(city_detail_name__contains=kwargs['region'])

            fundingList = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(campaign__city_detail_id=city[0].id,status=1).order_by('-id')[:6]
            donationList =  Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-id')[:6]
    

            campaignResult = Campaign.objects.annotate(campaign_participant_count=Count('campaignparticipant__campaign_id')).filter(city_detail_id=city[0].id,status=1).order_by('-campaign_participant_count')[:8]
            fundingResult = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(campaign__city_detail_id=city[0].id,status=1).order_by('-funding_sponsor_count')[:8]
            donationResult = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-donation_doner_count')[:8]

        else:    
            
            fundingList = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(status=1).order_by('-id')[:6]
            donationList =  Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-id')[:6]
    

            campaignResult = Campaign.objects.annotate(campaign_participant_count=Count('campaignparticipant__campaign_id')).filter(status=1).order_by('-campaign_participant_count')[:8]
            fundingResult = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(status=1).order_by('-funding_sponsor_count')[:8]
            donationResult = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-donation_doner_count')[:8]


        return render(request, 'funding_donation/home/_T001.html',{'fundingList':fundingList,'donationList':donationList,'campaignResult':campaignResult,'fundingResult':fundingResult,'donationResult':donationResult})
    

    def post(self, request, *args, **kwargs):
        
        try:
            data = json.loads(request.body)
            page = data['page']
            start = page * 9
            end = start + 9 
            data['city_detail_name'] = '동작구'

            if "전체" in data['city_detail_name']:
                print("문자열 안에 '전체'가 포함되어 있습니다.")

            elif "지역선택" in data['city_detail_name']:
                if data['type'] == 1:
                    # 펀딩 최신순
                    if data['catetype'] == 0:
                        dataList = Funding.objects.filter(status=1).order_by('-id')
                    # 펀딩 참여순
                    elif data['catetype'] == 1:
                        dataList = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(status=1).order_by('-funding_sponsor_count')

                elif data['type'] == 2:
                    # 기부 최신순
                    if data['catetype'] == 0:
                        dataList = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-id')
                    # 기부 참여순
                    elif data['catetype'] == 1:
                        dataList = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-donation_doner_count')

            else:
                city = CityDetail.objects.filter(city_detail_name__contains=data['city_detail_name'])
                
                if data['type'] == 1:
                    # 펀딩 최신순
                    if data['catetype'] == 0:
                        dataList = Funding.objects.filter(campaign__city_detail_id=city[0].id, status=1).order_by('-id')
                    # 펀딩 참여순
                    elif data['catetype'] == 1:
                        dataList = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(campaign__city_detail_id=city[0].id,status=1).order_by('-funding_sponsor_count')

                elif data['type'] == 2:
                    # 기부 최신순
                    if data['catetype'] == 0:
                        dataList = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-id')
                    # 기부 참여순
                    elif data['catetype'] == 1:
                        dataList = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(status=1).order_by('-donation_doner_count')


            cnt = dataList.count()
            dataList = dataList[start:end]
            queryset_json = serializers.serialize('json', dataList)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        return JsonResponse({'result': queryset_json,'cnt':cnt}, status=200)