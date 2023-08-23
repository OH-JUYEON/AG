from django.db import models

from AG.models import Period, Validity
from member.models import Member
from region.models import CityHeader, CityDetail  

# Create your models here.
class Campaign(Period, Validity):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    city_header = models.ForeignKey(CityHeader, null=True, on_delete=models.CASCADE)
    city_detail = models.ForeignKey(CityDetail, null=True, on_delete=models.CASCADE)
    campaign_title = models.CharField(null=False, max_length=256)
    campaign_category = models.CharField(null=False, max_length=100)
    campaign_description1 = models.CharField(null=False, max_length=100)
    campaign_description2 = models.CharField(null=False, max_length=100)
    campaign_description3 = models.CharField(null=False, max_length=100)
    campaign_image = models.ImageField(null=False, blank=False, upload_to='Campaign/%Y/%m/%d')
    campaign_content = models.CharField(null=False, max_length=10240)

    class Meta:
        db_table = "tbl_campaign"


class CampaignInquiry(Period):
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign_inquiry_type = models.CharField(null=False, max_length=10)
    campaign_inquiry_content = models.CharField(null=False, max_length=10240)
    campaign_inquiry_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_campaign_inquiry"


class CampaignInquiryAnswer(Period):
    campaign_inquiry = models.ForeignKey(CampaignInquiry, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign_inquiry_answer_content = models.CharField(null=False, max_length=1024)

    class Meta:
        db_table = "tbl_campaign_inquiry_answer"


class CampaignReview(Period):
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign_review_title = models.CharField(null=False, max_length=50)
    campaign_review_content = models.CharField(null=False, max_length=10240)
    campaign_review_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_campaign_review"


class CampaignParticipant(Period):
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign_participant_role = models.CharField(null=False, max_length=10)
    campaign_participant_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_campaign_participant"


class CampaignPhoto(Period):
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign_header_title = models.CharField(null=False, max_length=10)
    campaign_detail_image = models.ImageField(null=True, blank=False, upload_to='CampaignPhoto/%Y/%m/%d')

    class Meta:
        db_table = "tbl_campaign_photo"
