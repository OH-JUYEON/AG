from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from campaign.models import Campaign, CampaignReview, CampaignParticipant, CampaignPhoto
from region.models import CityHeader


# Create your views here.
class CampaignDetail(View):

    def get(self, request, *args, **kwargs):
        campaign_id = kwargs.get('campaign_id')
        campaign = get_object_or_404(Campaign, id=campaign_id)
        region_instance = get_object_or_404(CityHeader, id=campaign.city_header.id)
        participated = CampaignParticipant.objects.filter(campaign_id=campaign_id).count()
        reviews = CampaignReview.objects.filter(campaign_id=campaign_id)
        campaign_photos = CampaignPhoto.objects.filter(campaign_id=campaign_id)[:6]
        # member = request.session['member_id']

        context = {
            'campaign': campaign,
            'region': region_instance.city_name,
            'participated': participated,
            'review_count': reviews.count(),
        }

        photo_datas = []
        for campaign_photo in campaign_photos:
            photo_datas.append({
                'c_photo': campaign_photo.campaign_detail_image,
            })

        review_datas = []
        for review in reviews:
            review_datas.append({
                'r_campaignType': review.campaign.campaign_description1,
                'r_campaignArea': review.campaign.campaign_description2,
                'r_title': review.campaign_review_title,
                'r_content': review.campaign_review_content,
                'r_created_on': review.create_date,
                'r_written_by': review.member.member_name,
                'campaign': campaign,
            })

        context['review_datas'] = review_datas
        context['photo_datas'] = photo_datas



        return render(request, 'campaign/campaign-detail__001/_T002.html', context)
