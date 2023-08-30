from django.db import models

from AG.models import Period, Validity
from member.models import Member
from campaign.models import Campaign

# Create your models here.
class Funding(Period, Validity):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.CASCADE)
    funding_title = models.CharField(null=False, max_length=256)
    funding_minimum_amount = models.IntegerField(null=False, default=0)
    funding_description = models.CharField(null=False, max_length=256)
    funding_content = models.CharField(null=False, max_length=10240)
    funding_image = models.ImageField(null=False, blank=False, upload_to='Funding/%Y/%m/%d')
    funding_sub_image = models.ImageField(null=True, blank=False, upload_to='Funding/%Y/%m/%d')

    class Meta:
        db_table = "tbl_funding"


class FundingInquiry(Period):
    funding = models.ForeignKey(Funding, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_inquiry_type = models.CharField(null=False, max_length=10)
    funding_inquiry_content = models.CharField(null=False, max_length=10240)
    fundinginquiry_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_funding_inquiry"


class FundingInquiryAnswer(Period):
    funding_inquiry = models.ForeignKey(FundingInquiry, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_inquiry_answer_content = models.CharField(null=False, max_length=1024)

    class Meta:
        db_table = "tbl_funding_inquiry_answer"


class FundingReply(Period):
    funding = models.ForeignKey(Funding, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_reply_content = models.CharField(null=False, max_length=1024)
    funding_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_funding_reply"


class FundingSponsor(models.Model):
    funding = models.ForeignKey(Funding, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_amount = models.IntegerField(null=False, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_funding_sponsor"
