from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from django.http import HttpResponseRedirect

# Create your views here.
class AccountDel(View):

    def get(self, request, *args, **kwargs):
        id = request.session['member_id']

        user = Member.objects.get(id=id)
        user.status = 0
        user.save()
        
        return HttpResponseRedirect('/AG/logout/')  
