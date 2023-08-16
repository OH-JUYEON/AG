from django.db import models

from AG.models import Period, Validity
from member.models import Member


# Create your models here.
class FundingHeader(Period, Validity):
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_title = models.CharField(null=False, max_length=256)
    funding_minimum_amount = models.IntegerField(null=False, default=0)
    funding_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_funding_header"


class FundingDetail(models.Model):
    funding_header = models.ForeignKey(FundingHeader, null=False, on_delete=models.CASCADE)
    funding_description = models.CharField(null=False, max_length=256)
    funding_content = models.CharField(null=False, max_length=10240)
    funding_image = models.ImageField(null=False, blank=False, upload_to='FundingDetail/%Y/%m/%d')

    class Meta:
        db_table = "tbl_funding_detail"


class FundingInquiry(Period):
    funding_header = models.ForeignKey(FundingHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_inquiry_type = models.CharField(null=False, max_length=10)
    inquiry_content = models.CharField(null=False, max_length=10240)
    inquiry_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_funding_inquiry"


class FundingInquiryAnswer(Period):
    funding_inquiry = models.ForeignKey(FundingInquiry, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_inquiry_answer_content = models.CharField(null=False, max_length=1024)

    class Meta:
        db_table = "tbl_funding_inquiry_answer"


class FundingReply(Period):
    funding_header = models.ForeignKey(FundingHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_reply_content = models.CharField(null=False, max_length=1024)
    funding_status = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_funding_reply"


class FundingSponsor(models.Model):
    funding_header = models.ForeignKey(FundingHeader, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    funding_amount = models.IntegerField(null=False, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_funding_sponsor"
