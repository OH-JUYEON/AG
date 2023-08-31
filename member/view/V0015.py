import requests
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from region.models import CityHeader, CityDetail


# Create your views here.
class Login(View):

    def get(self, request, *args, **kwargs):
        url_path = request.GET.get('state')
        print(1234)
        print(url_path)
        code = request.GET.get("code")
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=f8ace2c69dab155b8e7caae84441295d&' \
                       'redirect_uri=http://localhost:8000/AG/oauth/redirectLogin&' \
                       f'code={code}'

        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)
        print(response.json())
        info = response.json().get('kakao_account')
        nickname = info.get('profile').get('nickname')
        thumbnail_image_url = info.get('profile').get('thumbnail_image_url')
        email = info.get('email')

        member = Member.objects.filter(member_email=email).first()
      
        if not member:
            city_detail_instance = CityDetail.objects.get(city_detail_name='강남구')
            city_header_instance = city_detail_instance.city_header

            member = Member.objects.create(member_email=email, member_name=nickname, city_header = city_header_instance, city_detail = city_detail_instance, status=1, member_image = thumbnail_image_url)
            request.session['member_id'] = member.id
            request.session['thumbnail_image_url'] = thumbnail_image_url
            request.session['access_token'] = access_token

            return redirect('/member/mypage/account')
        
        request.session['member_id'] = member.id
        request.session['thumbnail_image_url'] = thumbnail_image_url
        request.session['access_token'] = access_token


        for key, value in request.session.items():
            print(f"Key: {key}, Value: {value}")

        return redirect(url_path)

