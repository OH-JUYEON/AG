from django.urls import path, include
from django.views.generic import TemplateView
from donation.view import V0001, V0010, V0016

app_name = 'donation'

urlpatterns = [
    path("detail/<int:donation_id>/", V0001.DonationDetail.as_view(), name="detail"),
    path("detail/reply/", V0016.FundingReplyDetail.as_view(), name="detail"),
    path("inquiry/",
    include(
        [
            path("<int:donation_header_id>/", V0010.DonationInquiry.as_view(), name="inquiry"),
            path("", V0010.DonationInquiry.as_view(), name="answer"),
        ]
    ),),
]
