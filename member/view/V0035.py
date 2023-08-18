from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class NoInquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__008/_T008.html')