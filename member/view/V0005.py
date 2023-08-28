from django.db.models import Count, F
from django.shortcuts import render, redirect
from django.views import View

from campaign.models import Campaign, CampaignReview, CampaignParticipant
from donation.models import Donation
from funding.models import Funding, FundingSponsor
from member.models import Member
from region.models import CityHeader, CityDetail, SafetyScoreHeader


# Create your views here.
class Main(View):

    def get(self, request,  *args, **kwargs):

        # campaigns = Campaign.objects.all()[:6]
        # campaign_id_counts = CampaignParticipant.objects.values('campaign_id').annotate(campaign_id_count=Count('campaign_id')).order_by('-campaign_id_count')
        # sorted_campaign_ids = [item['campaign_id'] for item in campaign_id_counts]
        # campaigns = Campaign.objects.filter(id__in=sorted_campaign_ids)[:6]
        campaigns = Campaign.objects.annotate(campaign_participant_count=Count('campaignparticipant__campaign_id')).order_by('-campaign_participant_count')[:6]

        campaign_reviews = CampaignReview.objects.all().order_by('-id')[:3]
        fundings = Funding.objects.all().order_by('-id')[:6]
        donations = Donation.objects.all().select_related(
            'member',
            'member__city_header',
            'member__city_detail'
        ).annotate(
            city_name=F('member__city_header__city_name'),
            city_detail_name=F('member__city_detail__city_detail_name')
        ).order_by('-id')[:2]

        safety_scores = SafetyScoreHeader.objects.all().order_by('-safety_score')[:8]
        # image_instance = campaign_instance.objects.

        funding_counts = FundingSponsor.objects.values('funding_id').annotate(funding_count=Count('funding_id'))
        campaign_counts = CampaignParticipant.objects.values('campaign_id').annotate(campaign_count=Count('campaign_id'))
        safety_score_counts = SafetyScoreHeader.objects.values('city_header_id').annotate(safety_score_count=Count('city_header_id'))

        context = {
            'campaigns': campaigns,
            'campaign_reviews': campaign_reviews,
            'fundings': fundings,
            'donations': donations,
            'funding_counts': funding_counts,
            'campaign_counts': campaign_counts,
            'safety_scores': safety_scores,
            'safety_score_counts': safety_score_counts,

        }

        return render(request, 'AG/main/_T001.html',context )



    # def get(self, request, *args, **kwargs):
    #
    #
    #
    #     funding_data = {
    #
    #     }
    #
    #     return render(request, 'AG/main/_T001.html',{'context': funding_data} )

