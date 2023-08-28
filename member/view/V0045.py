from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from member.models import Member


# Create your views here.
class Unregister(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__009/_T009.html')
    