from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from donation.models import Donation


# Create your views here.
class DonationDetail(View):

    def get(self, request, *args, **kwargs):

        donation_id = kwargs.get('donation_id')

        donation = get_object_or_404(Donation, id=donation_id)

        context = {
            'donation': donation
        }

        # datas = {
        #     'donation_title': Donation.objects.values()[0]['donation_title'],
        #     'donation_minimum_amount': Donation.objects.values()[0]['donation_minimum_amount'],
        #     'donation_description': Donation.objects.values()[0]['donation_description'],
        #     'donation_content': Donation.objects.values()[0]['donation_content'],
        #     'donation_image': Donation.objects.values()[0]['donation_image']
        # }

        return render(request, 'funding_donation/donation__001/_T001.html', context)