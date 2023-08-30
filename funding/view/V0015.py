from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding
from donation.models import Donation

from django.db.models import Count, F, Max
from campaign.models import CampaignReview
import json
from django.http import JsonResponse
from pay.models import Pay


# Create your views here.
class FundingDetail(View):

    def get(self, request, *args, **kwargs):
        funding = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(id=kwargs['funding_header_id'],status=1)[0]
        reviews = CampaignReview.objects.filter(campaign=funding.campaign_id).count() 
        return render(request, 'funding_donation/funding__001/_T001.html',{'funding':funding,'reviews':reviews})
    
    # 0 - 펀딩 
    # 1 - 기부
    def post(self, request, **kwargs):
 
        # JSON 데이터를 파싱
        try:
            data = json.loads(request.body)

            all_pay_amount = Pay.objects.filter(member_id=request.session['member_id']).order_by('-id').first()
            pay = int(data['amount'])
            if all_pay_amount is not None:
                
                if all_pay_amount.pay_amount < int(data['amount']):
                    return JsonResponse({'result': 'charge'}, status=200)
                
                pay = all_pay_amount.pay_amount-int(data['amount'])
            else:
                return JsonResponse({'result': 'charge'}, status=200)


            if kwargs['type']:
                new_pay = Pay(
                    member_id=request.session['member_id'],
                    donation_id = int(data['id']),
                    pay_amount = pay,
                    pay_allowance=int(data['amount'])
                )
            else:
                new_pay = Pay(
                    member_id=request.session['member_id'],
                    funding_id = int(data['id']),
                    pay_amount = pay,
                    pay_allowance=int(data['amount'])
                )
                

            new_pay.save()
               
        except json.JSONDecodeError as e:
            return JsonResponse({'result': 'Invalid JSON'}, status=400)
        return JsonResponse({'result': 'OK'}, status=200)

