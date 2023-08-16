from django.db import models

from AG.models import Period


# Create your models here.
class CityHeader(models.Model):
    city_name = models.CharField(null=False, max_length=10)
    city_image = models.ImageField(null=False, blank=False, upload_to='CityHeader/%Y/%m/%d')

    class Meta:
        db_table = "tbl_city_header"


class CityDetail(models.Model):
    city_header = models.ForeignKey(CityHeader, null=False, on_delete=models.CASCADE)
    city_detail_name = models.CharField(null=False, max_length=10)

    class Meta:
        db_table = "tbl_city_detail"