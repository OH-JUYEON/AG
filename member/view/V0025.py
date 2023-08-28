from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NameModify(View):

    def get(self, request, *args, **kwargs):
       
        user = Member.objects.get(id=request.session['member_id']).member_name
        return render(request, 'mypage/mypage__003/_T003.html',{'name':user})
    

    def post(self, request):

        user = Member.objects.get(id=request.session['member_id'])
        user.member_name = request.POST.get('memberName')
        user.save()
      
        return HttpResponseRedirect('/member/mypage/account/')  
      
       