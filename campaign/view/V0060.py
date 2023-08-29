from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from campaign.models import CampaignReview
from member.models import Member


class CampaignReviewWrite(View):
    def get(self, request, *args, **kwargs):
        campaign_id = kwargs['campaign_id']
        context = {
            'campaign_id' : campaign_id
        }
        return render(request, 'campaign/campaign-review-write__001/_T007.html', {'campaign_id':campaign_id})

    def post(self, request, *args, **kwargs):
        datas = request.POST
        campaign_id = kwargs['campaign_id']
        datas = {

            'member_id' : request.session['member_id'],
            'campaign_id': campaign_id,
            'campaign_review_title': datas['campaign_review_title'],
            'campaign_review_content': datas['campaign_review_content'],
            'campaign_review_status': 1

        }

        campaign_review_image = request.FILES.get('campaign_review_image')
        if campaign_review_image:
            datas['campaign_review_image'] = campaign_review_image

        campain_review = CampaignReview.objects.create(**datas)


        return redirect('/member/mypage/activity/0')