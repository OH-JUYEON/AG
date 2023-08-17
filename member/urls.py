from django.urls import path, include
from django.views.generic import TemplateView
from member.view import V0001, V0010, V0020, V0030, V0040, V0050, V0060

app_name = 'member'

urlpatterns = [
    "mypage/",
    include(
        [
            path("", V0001.MyPage.as_view(), name="mypage"),
            path("account/", V0010.AccountModify.as_view(), name="account"),
            path("email/", V0020.EmailModify.as_view(), name="email"),
            path("activity/", V0030.ActivityModify.as_view(), name="activity"),
            path("cash/", V0040.Cash.as_view(), name="cash"),
            path("cashhistory/", V0050.CashHistory.as_view(), name="cashhistory"),
            path("inquiry/", V0060.Inquiry.as_view(), name="inquiry"),

        ]
    ),
]
