from django.shortcuts import render, redirect
from django.views import View

from campaign.models import CampaignParticipant, CampaignReview


# Create your views here.
class ActivityModify(View):

    def get(self, request, *args, **kwargs):

        joinList = CampaignParticipant.objects.filter(member_id=kwargs['member_id'],campaign_participant_status=1,campaign_participant_role='T')
        dataList = {}

        for index,key in enumerate(joinList):
            reviewstatus = 0;
            review = CampaignReview.objects.filter(member_id=kwargs['member_id'], campaign_header = key.campaign_header_id)
            if review:
                reviewstatus = 1;
 
            data={
                'campaign_title':key.campaign_header.campaign_title,
                'campaign_id':key.campaign_header_id,
                'campaign_description1':key.campaign_header.campaign_description1,
                'campaign_image':key.campaign_header.campaign_image.url,
                'reviewstatus':reviewstatus
            }
            
            dataList[index] = data
            len1 = index + 1

        createList = CampaignParticipant.objects.filter(member_id=kwargs['member_id'],campaign_participant_status=1,campaign_participant_role='L')
        dataList2 = {}

        for index,key in enumerate(createList):
            reviewstatus = 0;
            review = CampaignReview.objects.filter(member_id=kwargs['member_id'], campaign_header = key.campaign_header_id)
            if review:
                reviewstatus = 1;
 
            data={
                'campaign_title':key.campaign_header.campaign_title,
                'campaign_id':key.campaign_header_id,
                'campaign_description1':key.campaign_header.campaign_description1,
                'campaign_image':key.campaign_header.campaign_image.url,
                'reviewstatus':reviewstatus
            }
            
            dataList2[index] = data
            len2 = index + 1    

        return render(request, 'mypage/mypage__004/_T004.html',{'context1':dataList,'len1':len1,'context2':dataList2,'len2':len2})