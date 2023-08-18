from django.urls import path, include
from django.views.generic import TemplateView
from pay.view import V0001

app_name = 'pay'

urlpatterns = [
    path("", V0001.Pay.as_view(), name="pay"),
]
