from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class CashHistory(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__006/_T006.html')