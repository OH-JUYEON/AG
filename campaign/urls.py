from django.urls import path, include
from django.views.generic import TemplateView
from campaign.view import V0001, V0010, V0020, V0030, V0040, V0050, V0060

app_name = 'campaign'

urlpatterns = [
    path("", V0001.CampaignList.as_view(), name="list"),
    # path("detail/<int:donation_header_id>/", V0010.CampaignDetail.as_view(), name="detail"),
    path("detail/<int:campaign_id>/", V0010.CampaignDetail.as_view(), name="detail"),
    path("write/", V0020.CampaignWrite.as_view(), name="write"),
    # path("review/<int:campaign_header_id>/", V0040.CampaignReview.as_view(), name="review"),
    path("review/", V0040.CampaignReview.as_view(), name="review"),
    # path("photo/<int:campaign_header_id>/", V0050.CampaignPhoto.as_view(), name="photo"),
    path("photo/", V0050.CampaignPhoto.as_view(), name="photo"),
    path("reviewWrite/<int:campaign_id>/", V0060.CampaignReviewWrite.as_view(), name="reviewWrite"),
    path("inquiry/",
         include(
             [
                 path("<int:campaign_header_id>/", V0030.CampaignInquiry.as_view(), name="inquiry"),
                 path("", V0030.CampaignInquiry.as_view(), name="answer"),
             ]
    ),),


]
