from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class Cash(View):

    def get(self, request, *args, **kwargs):
        member_id = request.session['member_id']
        path=''  
        if request.GET.get('path'):
            path = request.GET.get('path')
             
        return render(request, 'mypage/mypage__005/_T005.html',{'member_id':member_id,'path':path})