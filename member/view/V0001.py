from django.shortcuts import render, redirect
from django.views import View
from member.models import Member

# Create your views here.
class MyPage(View):

    def get(self, request, *args, **kwargs):
        if 'member_id' in request.session:
            member_name = Member.objects.get(id=request.session['member_id']).member_name
            return render(request, 'mypage/mypage__001/_T001.html',{'img':request.session['thumbnail_image_url'],'name':member_name})
        else:
            return redirect('/AG/login/')
        