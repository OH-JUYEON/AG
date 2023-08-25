from django.shortcuts import render, redirect
from django.views import View
from region.models import SafeRegion, SafetyScoreHeader
from campaign.models import Campaign,CampaignParticipant
import os
import csv
import pandas

# Create your views here.
class SafetyScoreDetail(View):

    def get(self, request, *args, **kwargs):

        dataObj = SafeRegion.objects.get(city_header_id=kwargs['region'])

        campaignObj = Campaign.objects.filter(city_header_id=dataObj.city_header_id).order_by('-id')[:3]
    
        count = CampaignParticipant.objects.filter(campaign__city_header=dataObj.city_header_id).count()
        
        score = SafetyScoreHeader.objects.all()

        # 현재 스크립트 파일의 디렉터리 경로를 가져옵니다.
        script_dir = os.path.dirname(__file__)

        # 읽을 파일의 상대 경로 또는 절대 경로를 생성합니다.
        file_path = os.path.join(script_dir, 'safe.csv')  # 파일 이름을 'safe.csv'로 가정

     

        file = open(file_path, 'r', encoding='utf-8')
        reader = csv.reader(file)

        dataset = []

        for line in reader:
            dataset.append(line)

        pandas.set_option('display.max_rows', None)
        df = pandas.DataFrame(dataset)
        df[6] = df[6].astype(int)
        df = df.sort_values(by=6, ascending=True)
        data = df[[0, 1, 2, 3, 4, 5, 6, 7]]
        data = data[data[6]!=0]
        data = data.groupby(1)[6].mean()

        
        for key in score:
            _index_ = data.index.get_loc(key.city_header.city_name)

            data._values[_index_] = data._values[_index_] - key.safety_score

        

        sorted_grouped = data.sort_values()
        # '인천광역시'를 찾아 해당 인덱스(순위)를 가져옴
        incheon_index = sorted_grouped.index.get_loc(dataObj.city_header.city_name)

        # 해당 인덱스(순위)를 사용하여 값을 가져옴
        incheon_value = sorted_grouped._values[incheon_index]


        dataInfo = {
            'city_name':dataObj.city_header.city_name,
            'city_img':dataObj.city_header.city_image.url,
            'safe_region_description':dataObj.safe_region_description,
            'safe_region_description2':dataObj.safe_region_description2,
            'safe_region_url':dataObj.safe_region_url,
            'safe_region_info':dataObj.safe_region_info,
            'safe_region_content':dataObj.safe_region_content,
            'ranking':incheon_index+1,
            'ranking_val':round(incheon_value,2),
            'cnt':count
        }
        
                
        return render(request, 'region/detail/_T001.html',{'dataObj':dataInfo,'campaignObj':campaignObj})

        