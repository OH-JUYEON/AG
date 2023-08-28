from django.urls import path, include
from django.views.generic import TemplateView
from funding.view import V0001, V0010, V0020, V0030, V0040

app_name = 'funding'

urlpatterns = [
    path("donation/", V0001.FundingDonationList.as_view(), name="funding"),
    path("search/", V0040.Search.as_view(), name="funding"),
    path("detail/<int:funding_header_id>/", V0010.FundingDetail.as_view(), name="detail"),
    path("write/<int:funding_header_id>/", V0020.FundingWrite.as_view(), name="write"),
    path("inquiry/",
    include(
        [
            path("<int:funding_header_id>/", V0030.FundingInquiry.as_view(), name="inquiry"),
            path("", V0030.FundingInquiry.as_view(), name="answer"),
        ]
    ),),
]
