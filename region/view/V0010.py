from django.shortcuts import render, redirect
from django.views import View
from region.models import SafeRegion, SafetyScoreHeader
from campaign.models import Campaign,CampaignParticipant
import os
import csv
import pandas
import numpy as np
import json
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
        df[[6, 7, 8, 9, 10, 11, 12, 13]] = df[[6, 7, 8, 9, 10, 11, 12, 13]].astype(int)

        df = df.sort_values(by=6, ascending=True)
        data_obj = df[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
        data_obj = data_obj[data_obj[6]!=0]


        data =  data_obj.groupby(1)[[6,7,8,9,10,11,12,13]].mean()
        sum_of_columns = data[[7, 8, 9, 10, 11, 12, 13]].sum(axis=1)

        # 각 행에 대한 백분율을 계산합니다.
        percentage_of_rows = data[[7, 8, 9, 10, 11, 12, 13]].div(sum_of_columns, axis=0) * 100

        # 결과를 기존 DataFrame에 추가합니다.
        data[7] = percentage_of_rows[7]
        data[8] = percentage_of_rows[8]
        data[9] = percentage_of_rows[9]
        data[10] = percentage_of_rows[10]
        data[11] = percentage_of_rows[11]
        data[12] = percentage_of_rows[12]
        data[13] = percentage_of_rows[13]


        
        for key in score:
            _index_ = data.index.get_loc(key.city_header.city_name)

            data._values[_index_] = data._values[_index_] - key.safety_score

        

        sorted_grouped = data.sort_values(by=6)
        # '인천광역시'를 찾아 해당 인덱스(순위)를 가져옴
        city_index = sorted_grouped.index.get_loc(dataObj.city_header.city_name)

        # 해당 인덱스(순위)를 사용하여 값을 가져옴
        incheon_value = sorted_grouped._values[city_index][0]

        ranking = {
            '강원도':sorted_grouped._values[sorted_grouped.index.get_loc('강원도')][0],
            '경기도':sorted_grouped._values[sorted_grouped.index.get_loc('경기도')][0],
            '경상남도':sorted_grouped._values[sorted_grouped.index.get_loc('경상남도')][0],
            '경상북도':sorted_grouped._values[sorted_grouped.index.get_loc('경상북도')][0],
            '광주':sorted_grouped._values[sorted_grouped.index.get_loc('광주광역시')][0],
            '대구':sorted_grouped._values[sorted_grouped.index.get_loc('대구광역시')][0],
            '대전':sorted_grouped._values[sorted_grouped.index.get_loc('대전광역시')][0],
            '부산':sorted_grouped._values[sorted_grouped.index.get_loc('부산광역시')][0],
            '서울':sorted_grouped._values[sorted_grouped.index.get_loc('서울특별시')][0],
            '세종':sorted_grouped._values[sorted_grouped.index.get_loc('세종특별자치시')][0],
            '울산':sorted_grouped._values[sorted_grouped.index.get_loc('울산광역시')][0],
            '인천':sorted_grouped._values[sorted_grouped.index.get_loc('인천광역시')][0],
            '전라남도':sorted_grouped._values[sorted_grouped.index.get_loc('전라남도')][0],
            '전라북도':sorted_grouped._values[sorted_grouped.index.get_loc('전라북도')][0],
            '제주도':sorted_grouped._values[sorted_grouped.index.get_loc('제주특별자치도')][0],
            '충청남도':sorted_grouped._values[sorted_grouped.index.get_loc('충청남도')][0],
            '충청북도':sorted_grouped._values[sorted_grouped.index.get_loc('충청북도')][0]
        }

        dataInfo = {
            'city_name':dataObj.city_header.city_name,
            'city_img':dataObj.city_header.city_image.url,
            'safe_region_description':dataObj.safe_region_description,
            'safe_region_description2':dataObj.safe_region_description2,
            'safe_region_url':dataObj.safe_region_url,
            'safe_region_info':dataObj.safe_region_info,
            'safe_region_content':dataObj.safe_region_content,
            'ranking':city_index+1,
            'ranking_val':round(incheon_value,2),
            'cnt':count
        }
        
        data_dict = {str(index): round(value, 2) for index, value in enumerate(sorted_grouped._values[city_index])}
       
        return render(request, 'region/detail/_T001.html',{'dataObj':dataInfo,'campaignObj':campaignObj,'ranking':json.dumps(ranking),'ranking_detail':json.dumps(data_dict)})

        