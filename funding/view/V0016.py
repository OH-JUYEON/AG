from django.shortcuts import render, redirect
from django.views import View
from donation.models import Donation, DonationReply
from django.db.models import Count, F, Max
import json
from django.http import JsonResponse
from pay.models import Pay


# Create your views here.
class FundingReplyDetail(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding_donation/funding__001/_T001.html')
    
    # 0 - 펀딩 
    # 1 - 기부
    def post(self, request, **kwargs):
 
        # JSON 데이터를 파싱
        try:
            data = json.loads(request.body)
            content = data['content'].replace(" ", "")
            
            data = DonationReply.objects.create(
                member_id=request.session['member_id'],
                donation_id = int(data['id']),
                donation_reply_content = content,
                donation_status=1
            )

            # new_data.save()

            # data = FundingReply.objects.filter(member_id=request.session['member_id'], funding_id=int(data['id'])).first()


          
        except json.JSONDecodeError as e:
            return JsonResponse({'result': 'Invalid JSON'}, status=400)
        return JsonResponse({'result': 'OK','name':data.member.member_name,'date':data.create_date.strftime('%Y.%m.%d'),'content':data.donation_reply_content}, status=200)

