from django.db import models


class Period(models.Model):
    create_date = models.DateTimeField(null=True, auto_now_add=True)
    update_date = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class Validity(models.Model):
    status = models.SmallIntegerField(null=False, default=0)
    started_on = models.DateTimeField(null=True, auto_now_add=True)
    ends_on = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True
