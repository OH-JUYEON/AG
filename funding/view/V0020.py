from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

from funding.models import Funding
from member.models import Member



# Create your views here.
class FundingWrite(View):

    def get(self, request, *args, **kwargs):
        campaign_id = kwargs['campaign_id']
        context = {
            'campaign_id': campaign_id
        }
        return render(request, 'funding_donation/write__001/_T003.html', {'campaign_id':campaign_id})

    def post(self, request, *args, **kwargs):
        datas = request.POST
        campaign_id = kwargs['campaign_id']

        member_id = request.session['member_id']
        member = Member.objects.get(id=member_id)

        started_on_string = request.POST['started_on']
        started_on = datetime.strptime(started_on_string, '%Y-%m-%dT%H:%M')
        formatted_started_on = started_on.strftime('%Y-%m-%d %H:%M:%S')

        ends_on_string = request.POST['ends_on']
        ends_on = datetime.strptime(ends_on_string, '%Y-%m-%dT%H:%M')
        formatted_ends_on = ends_on.strftime('%Y-%m-%d %H:%M:%S')

        raw_value=request.POST['funding_minimum_amount']
        funding_minimum_amount = int(''.join(raw_value.split(',')))

        datas = {

            'member_id': member_id,
            'funding_title': datas['funding_title'],
            'funding_content': datas['funding_content'],
            'funding_description': datas['funding_description'],
            'campaign_id': campaign_id,
            'started_on' : formatted_started_on,
            'ends_on': ends_on,
            'funding_minimum_amount': funding_minimum_amount ,

            'status': 1
        }



        funding_image = request.FILES.get('funding_image')
        if funding_image:
            datas['funding_image'] = funding_image

        funding_sub_image = request.FILES.get('funding_sub_image')
        if funding_sub_image:
            datas['funding_sub_image'] = funding_sub_image


        funding = Funding.objects.create(**datas)





        return redirect('/member/mypage/activity/1')