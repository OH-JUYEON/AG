from django.shortcuts import render, redirect
from django.views import View
from funding.models import Funding, FundingInquiry, FundingReply
from django.db.models import Count, F
from campaign.models import CampaignReview
import json
from django.http import JsonResponse


# Create your views here.
class FundingDetail(View):

    def get(self, request, *args, **kwargs):
        funding = Funding.objects.annotate(funding_sponsor_count=Count('fundingsponsor__funding_id')).filter(id=kwargs['funding_header_id'],status=1)[0]
        reviews = CampaignReview.objects.filter(campaign=funding.campaign_id).count()
        replay = FundingReply.objects.filter(funding_id = kwargs['funding_header_id'], funding_status=1).order_by('-id') 
        return render(request, 'funding_donation/funding__001/_T001.html',{'funding':funding,'reviews':reviews,'replay':replay})
    
    
    def post(self, request, **kwargs):
 
        # JSON 데이터를 파싱
        try:
            data = json.loads(request.body)
            
            new_funding = FundingInquiry(
                funding_inquiry_type=int(data['type']),  
                funding_inquiry_content=data['content'],
                fundinginquiry_status=1,
                member_id = request.session['member_id'],
                funding_id = int(data['id'])
            )
            
            # 데이터베이스에 저장
            new_funding.save()
        except json.JSONDecodeError as e:
            return JsonResponse({'result': 'Invalid JSON'}, status=400)
        return JsonResponse({'result': 'OK'}, status=200)

