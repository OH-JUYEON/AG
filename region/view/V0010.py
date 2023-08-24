from django.shortcuts import render, redirect
from django.views import View
from region.models import SafeRegion
from campaign.models import Campaign
import os
import csv
import pandas

# Create your views here.
class SafetyScoreDetail(View):

    def get(self, request, *args, **kwargs):

        dataObj = SafeRegion.objects.get(city_header_id=kwargs['region'])

        dataInfo = {
            'city_name':dataObj.city_header.city_name,
            'city_img':dataObj.city_header.city_image.url,
            'safe_region_description':dataObj.safe_region_description,
            'safe_region_description2':dataObj.safe_region_description2,
            'safe_region_url':dataObj.safe_region_url,
            'safe_region_info':dataObj.safe_region_info,
            'safe_region_content':dataObj.safe_region_content,
        }

        campaignObj = Campaign.objects.all().order_by('-id')[:3]
    


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
        
        print(data.groupby(1))
                
        return render(request, 'region/detail/_T001.html',{'dataObj':dataInfo,'campaignObj':campaignObj})
