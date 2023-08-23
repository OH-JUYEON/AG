from django.shortcuts import render, redirect
from django.views import View

from campaign.models import CampaignParticipant, CampaignReview
from region.models import CityDetail


# Create your views here.
# inquiry_type
# 0-답변대기
# 1-답변완료

class ReviewList(View):

    def get(self, request, *args, **kwargs):     
        page = 1
        start = page * 5
        end = start + 5 
        reviewList = CampaignReview.objects.filter(member_id=kwargs['member_id'],campaign_review_status=1).order_by('-id')[:5]
        dataList5 = {}

        for index,key in enumerate(reviewList):
            city = CityDetail.objects.filter(id=key.campaign.city_detail_id)

            data={
                'campaign_title':key.campaign_review_title,
                'campaign_review_content':key.campaign_review_content,
                'campaign_id':key.campaign_id,
                'campaign_image':key.campaign.campaign_image.url,
                'header_name':city[0].city_header.city_name,
                'detail_name':city[0].city_detail_name
            }
            
            dataList5[index] = data
                       

        return render(request, 'mypage/mypage__007/_T007.html')
    


    # def post(self, request):

    #      # JSON 데이터를 파싱
    #     try:
    #         data = json.loads(request.body)
    #         city_header = CityHeader.objects.get(city_name=data['city_header_name'])
    #         city_detail = CityDetail.objects.get(city_detail_name=data['city_detail_name'])
            
    #         user = Member.objects.get(id=data['member_id'])
    #         user.city_header_id = city_header.id
    #         user.city_detail_id = city_detail.id
    #         user.save()

    #     except json.JSONDecodeError as e:
    #         return JsonResponse({'error': 'Invalid JSON'}, status=400)

    #     return JsonResponse({'result': 'OK'}, status=200)