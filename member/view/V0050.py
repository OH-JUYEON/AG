from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from pay.models import Pay

# Create your views here.
class CashHistory(View):
    # ag_type
    # 0 - 충전
    # 1 - 펀딩
    # 2 - 기부
    def get(self, request, *args, **kwargs):
        member_id=request.session['member_id']
        pay_obj = Pay.objects.filter(member_id=member_id).order_by('-id')
        dataList = {}
        ag_type=0
        for index,key in enumerate(pay_obj):
            if key.funding_id:
                ag_type=1
            elif key.donation_id:
                ag_type=2 
            data={
                    'date':key.create_date.strftime('%Y.%m.%d'),
                    'type':ag_type,
                    'pay_amount':key.pay_amount,
                    'pay_allowance':key.pay_allowance
                }
            
            dataList[index] = data
        user_pay_amount = pay_obj[0].pay_amount

        return render(request, 'mypage/mypage__006/_T006.html',{'context':dataList,'user_pay_amount':user_pay_amount})
    

    def post(self, request, *args, **kwargs):

        id = request.session['member_id']
        pay = int(request.POST.get("pay"))
        pay_amount = 0
        pay_obj = Pay.objects.filter(member_id=id).order_by('-id')
        if pay_obj:
           pay_amount = pay_obj[0].pay_amount

        Pay.objects.create(
            member_id=id, pay_allowance=pay, pay_amount=pay_amount+pay
        )



        return render(request, 'mypage/mypage__006/_T006.html')