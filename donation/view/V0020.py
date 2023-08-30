from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class DonationInquiry(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'donation/donation__002/_T002.html')

    def post(self, request, *args, **kwargs):
        return redirect('/donation/inquiry')
