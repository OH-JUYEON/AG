from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class EmailModify(View):

    def get(self, request, *args, **kwargs):
        # data = request.POST.get('member_id', '') 
        # data = request.POST.get('memberEmail', '') 
        
        return render(request, 'mypage/mypage__003/_T003.html',{'email':request.GET.get('email', ''), 'id':request.GET.get('id', '')})
    

    def post(self, request):

        user = Member.objects.get(id=request.POST.get('member_id'))
        user.member_email = request.POST.get('memberEmail')
        user.save()
      
        return HttpResponseRedirect('/member/mypage/account/')  
      
       