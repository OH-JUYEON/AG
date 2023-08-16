from django.urls import path
from django.views.generic import TemplateView

app_name = 'funding'



urlpatterns = [
    path('', TemplateView.as_view(template_name='mypage/mypage__001/_T001.html'), name='success'),
 ]

