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

    class Meta:
        db_table = "tbl_member"
