import requests
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member





class Logout(View):

    def get(self, request, *args, **kwargs):
        path = request.GET.get("path")

        headers = {
            'Authorization': f"Bearer {request.session['access_token']}",
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }


        response = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)


        request.session.flush()


        response.cookies.clear_session_cookies()



        return redirect('/AG')
