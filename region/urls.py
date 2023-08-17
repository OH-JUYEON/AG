from django.urls import path
from django.views.generic import TemplateView
from region.view import V0001, V0010

app_name = 'region'

urlpatterns = [
    path("", V0001.SafetyScoreHeader.as_view(), name="region"),
    path("detail/", V0010.SafetyScoreDetail.as_view(), name="detail"),
]
