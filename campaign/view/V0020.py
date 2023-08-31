from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime


from member.models import Member
from campaign.models import Campaign
from campaign.models import CampaignParticipant

# Create your views here.
class CampaignWrite(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'campaign/campaign-write__001/_T003.html')

    def post(self, request, *args, **kwargs):
        datas = request.POST
        member_id = request.session['member_id']
        member = Member.objects.get(id=member_id)

        started_on_string = request.POST['started_on']
        started_on = datetime.strptime(started_on_string, '%Y-%m-%dT%H:%M')
        formatted_started_on = started_on.strftime('%Y-%m-%d %H:%M:%S')


        ends_on_string = request.POST['ends_on']
        ends_on = datetime.strptime(ends_on_string, '%Y-%m-%dT%H:%M')
        formatted_ends_on = ends_on.strftime('%Y-%m-%d %H:%M:%S')

        datas = {

            'member_id': member_id,
            'campaign_title': datas['campaign_title'],
            'campaign_content': datas['campaign_content'],
            'campaign_category': datas['campaign_category'],
            'campaign_description3': datas['campaign_description3'],
            'started_on' : formatted_started_on,
            'ends_on': ends_on,
            'city_header_id' : member.city_header_id,
            'city_detail_id' : member.city_detail_id,

            'status': 1
        }



        campaign_image = request.FILES.get('campaign_image')
        if campaign_image:
            datas['campaign_image'] = campaign_image


        campaign = Campaign.objects.create(**datas)


        CampaignParticipant.objects.create(
            campaign_id=campaign.id,
            member_id=member_id,
            campaign_participant_role='L',
            campaign_participant_status=1
        )
        # campaign = Campaign.objects.create(
        #     member_id=request.session['member_id'],
        #     campaign_title=datas['campaign_title'],
        #     campaign_content=datas['campaign_content'],
        #     campaign_category=datas['campaign_category'],
        #     campaign_description3=datas['campaign_description3'],
        #     started_on=formatted_started_on,
        #     ends_on=formatted_ends_on,
        #     campaign_image=campaign_image,
        #     city_header_id= Member.objects.get(member_id=request.session['member_id']).city_header_id,
        #     city_detail= Member.objects.get(member_id=request.session['member_id']).city_detail_id,
        #     campaign_status=1
        # )


        return redirect('/campaign')



