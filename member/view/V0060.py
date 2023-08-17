from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class Inquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__007/_T007.html')