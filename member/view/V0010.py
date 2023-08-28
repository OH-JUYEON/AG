from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from region.models import CityHeader, CityDetail

from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class AccountModify(View):

    def get(self, request, *args, **kwargs):
        if 'member_id' in request.session:
            user = Member.objects.get(id=request.session['member_id'])
            data={
                    'member_id':user.id,
                    'member_name':user.member_name,
                    'member_email':user.member_email,
                    'member_image':request.session['thumbnail_image_url'],
                    'city_name':user.city_header.city_name,
                    'city_detail_name':user.city_detail.city_detail_name,
                }
                
            return render(request, 'mypage/mypage__002/_T002.html',{'context':data})
        
        else:
            return redirect('/AG/login/')

    def post(self, request):

         # JSON 데이터를 파싱
        try:
            data = json.loads(request.body)
            city_header = CityHeader.objects.get(city_name=data['city_header_name'])
            city_detail = CityDetail.objects.get(city_detail_name=data['city_detail_name'])
            
            user = Member.objects.get(id=data['member_id'])
            user.city_header_id = city_header.id
            user.city_detail_id = city_detail.id
            user.save()

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        return JsonResponse({'result': 'OK'}, status=200)
     
#         user.member_email = request.POST.get('memberEmail')
#         user.save()
      
#         return HttpResponseRedirect('/member/mypage/account/')  



# def change_password(request):
#     logger.info('change_password() Start')

#     try:
#         cur_password = request.POST['curPassword']
#         new_password = request.POST['newPassword']
#         # new_password_re = request.POST['newPasswordRe']
#         user_id = request.session.get('user_id')

#         logger.info(f'change_password() Target user [ user_id = {user_id} ]')
#     except Exception as e:
#         logger.error(f'change_password() Failed to get parameter. [ {e} ]')
#         return JsonResponse(data=json.dumps({'result': 'NG'}, ensure_ascii=False), safe=False, status=500)
