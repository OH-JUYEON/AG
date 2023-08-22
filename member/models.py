from django.db import models
from AG.models import Period
from region.models import CityHeader, CityDetail


# Create your models here.
class Member(Period):
    city_header = models.ForeignKey(CityHeader, null=False, on_delete=models.CASCADE)
    city_detail = models.ForeignKey(CityDetail, null=False, on_delete=models.CASCADE)
    member_name = models.CharField(null=False, max_length=10)
    member_address = models.CharField(null=False, max_length=100)
    member_email = models.CharField(null=False, max_length=100)
    member_grade = models.SmallIntegerField(default=None, null=True)
    member_image = models.ImageField(null=False, blank=False, upload_to='Member/%Y/%m/%d')
    status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_member"

class Notice(Period):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    notice_title =  models.CharField(null=False, max_length=1024)
    notice_content = models.CharField(null=False, max_length=10240)
    notice_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_notice"


class Inquiry(Period):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    inquiry_title = models.CharField(null=False, max_length=1024)
    inquiry_content = models.CharField(null=False, max_length=10240)
    inquiry_content =models.ImageField(null=False, blank=False, upload_to='Inquiry/%Y/%m/%d')
    inquiry_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_inquiry"


class InquiryAnswer(Period):
    funding_inquiry = models.ForeignKey(Inquiry, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    inquiry_answer_content = models.CharField(null=False, max_length=1024)

    class Meta:
        db_table = "tbl_inquiry_answer"        