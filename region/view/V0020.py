from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class FundingWrite(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'funding/funding__003/_T003.html')