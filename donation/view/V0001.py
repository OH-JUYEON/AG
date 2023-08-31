from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Count, F
from donation.models import Donation, DonationReply, DonationInquiry
import json
from django.http import JsonResponse

# Create your views here.
class DonationDetail(View):

    def get(self, request, *args, **kwargs):

        donation = Donation.objects.annotate(donation_doner_count=Count('donationdoner__donation_id')).filter(id=kwargs['donation_id'],status=1)
        data = donation[0]
        cnt = donation.count()
        
        # reviews = DonationReply.objects.filter().count()
        replay = DonationReply.objects.filter(donation_id = kwargs['donation_id'], donation_status=1).order_by('-id') 
        return render(request, 'funding_donation/donation__001/_T001.html',{'donation':data,'replay':replay,'cnt':cnt})
           

        # donation_id = kwargs.get('donation_id')

        # donation = get_object_or_404(Donation, id=donation_id)

        # donation_instance = Donation.objects.get(pk=donation_id)
        # writer_instance = donation_instance.member

        # context = {
        #     'donation': donation,
        #     'writer': writer_instance.member_name,
        #     'donation_id': donation_id
        # }

        # return render(request, 'funding_donation/donation__001/_T001.html', context)
    
    def post(self, request, **kwargs):
 
        # JSON 데이터를 파싱
        try:
            data = json.loads(request.body)
            
            new_funding = DonationInquiry(
                donation_inquiry_type=int(data['type']),  
                donation_inquiry_content=data['content'],
                donation_inquiry_status=1,
                member_id = request.session['member_id'],
                donation_id = int(data['id'])
            )
            
            # 데이터베이스에 저장
            new_funding.save()
        except json.JSONDecodeError as e:
            return JsonResponse({'result': 'Invalid JSON'}, status=400)
        return JsonResponse({'result': 'OK'}, status=200)


