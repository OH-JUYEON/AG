from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class MyPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__001/_T001.html')