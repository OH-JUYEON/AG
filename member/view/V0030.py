from django.shortcuts import render, redirect
from django.views import View

from campaign.models import CampaignParticipant, CampaignReview
from funding.models import FundingSponsor
from donation.models import DonationDoner


from region.models import CityDetail



# Create your views here.
class ActivityModify(View):

    def get(self, request, *args, **kwargs):
        member_id=request.session['member_id']
        len1, len2, len3, len4 = 0, 0, 0, 0
        joinList = CampaignParticipant.objects.filter(member_id=member_id,campaign_participant_status=1,campaign_participant_role='T')
        dataList = {}

        for index,key in enumerate(joinList):
            reviewstatus = 0
            review = CampaignReview.objects.filter(member_id=member_id, campaign = key.campaign_id)
            if review:
                reviewstatus = 1
 
            data={
                'campaign_title':key.campaign.campaign_title,
                'campaign_id':key.campaign_id,
                'campaign_description1':key.campaign.campaign_description1,
                'campaign_image':key.campaign.campaign_image.url,
                'reviewstatus':reviewstatus
            }
            
            dataList[index] = data
            len1 = index + 1

        createList = CampaignParticipant.objects.filter(member_id=member_id,campaign_participant_status=1,campaign_participant_role='L')
        dataList2 = {}

        for index,key in enumerate(createList):
            reviewstatus = 0
            review = CampaignReview.objects.filter(member_id=member_id, campaign = key.campaign_id)
            if review:
                reviewstatus = 1
 
            data={
                'campaign_title':key.campaign.campaign_title,
                'campaign_id':key.campaign_id,
                'campaign_description1':key.campaign.campaign_description1,
                'campaign_image':key.campaign.campaign_image.url,
                'reviewstatus':reviewstatus
            }
            
            dataList2[index] = data
            len2 = index + 1   


        fundingList = FundingSponsor.objects.filter(member_id=member_id)
        dataList3 = {}

        for index,key in enumerate(fundingList):

            data={
                'funding_title':key.funding.funding_title,
                'funding_id':key.funding_id,
                'funding_amount':key.funding_amount,
                'funding_image':key.funding.funding_image.url,
            }
            
            dataList3[index] = data
            len3 = index + 1  

        donationList = DonationDoner.objects.filter(member_id=member_id)
        dataList4 = {}

        for index,key in enumerate(donationList):

            data={
                'donation_title':key.donation.donation_title,
                'donation_id':key.id,
                'donate_amount':key.donate_amount,
                'donation_image':key.donation.donation_image.url,
            }
            
            dataList4[index] = data
            len4 = index + 1  

        reviewList = CampaignReview.objects.filter(member_id=member_id,campaign_review_status=1).order_by('-id')[:5]
        dataList5 = {}

        for index,key in enumerate(reviewList):
            city = CityDetail.objects.filter(id=key.campaign.city_detail_id)

            data={
                'campaign_title':key.campaign_review_title,
                'campaign_review_content':key.campaign_review_content,
                'campaign_id':key.campaign_id,
                'campaign_image':key.campaign.campaign_image.url,
                'header_name':city[0].city_header.city_name,
                'detail_name':city[0].city_detail_name
            }
            
            dataList5[index] = data
                  

        return render(request, 'mypage/mypage__004/_T004.html',{'context1':dataList,'len1':len1,'context2':dataList2,'len2':len2,'context3':dataList3,'len3':len3,'context4':dataList4,'len4':len4,'context5':dataList5,'type':kwargs.get('type')})