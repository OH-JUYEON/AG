from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class AccountModify(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'mypage/mypage__002/_T002.html')
