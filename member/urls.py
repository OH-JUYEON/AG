from django.urls import path, include
from django.views.generic import TemplateView
from member.view import V0001, V0010, V0020, V0030, V0035, V0040, V0045, V0050, V0060, V0070, V0055, V0065, V0025, V0075, V0080

app_name = 'member'

urlpatterns = [
    path("mypage/",
    include(
        [
            path("", V0001.MyPage.as_view(), name="mypage"),
            path("account/", V0010.AccountModify.as_view(), name="account"),
            # path("email/", V0020.EmailModify.as_view(), name="email"),
            path("name/", V0025.NameModify.as_view(), name="email"),
            path("account/delete/", V0055.AccountDel.as_view(), name="account"),
            path("activity/review/<int:page>/", V0065.ReviewList.as_view(), name="activityreview"),
            path("activity/<int:type>/", V0030.ActivityModify.as_view(), name="activity"),
            path("cash/", V0040.Cash.as_view(), name="cash"),
            path("cashhistory/", V0050.CashHistory.as_view(), name="cashhistory"),
            path("inquiry/", V0060.InquiryList.as_view(), name="inquiry"),
            path("faq/", V0070.Faq.as_view(), name="faq"),
            path("noinquiry/", V0035.NoInquiry.as_view(), name="noinquiry"),
            path("unregister/", V0045.Unregister.as_view(), name="unregister"),
            path("notice/", V0075.NoticeView.as_view(), name="notice"),
            path("notice-detail/<int:id>/", V0080.NoticeDetail.as_view(), name="notice-detail"),


        ]
    ))
]
