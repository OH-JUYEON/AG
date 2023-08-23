from django.db import models
from funding.models import Funding
from donation.models import Donation
from member.models import Member
from AG.models import Period

# Create your models here.

class Pay(Period):
    member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    funding = models.ForeignKey(Funding, null=True, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, null=True, on_delete=models.CASCADE)
    pay_amount = models.IntegerField(null=True)
    pay_allowance = models.IntegerField(null=True)

    class Meta:
        db_table = "tbl_pay"         