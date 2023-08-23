from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from donation.models import Donation


# Create your views here.
class DonationDetail(View):

    def get(self, request, *args, **kwargs):

        donation_id = kwargs.get('donation_id')

        donation = get_object_or_404(Donation, id=donation_id)

        donation_instance = Donation.objects.get(pk=donation_id)
        writer_instance = donation_instance.member

        context = {
            'donation': donation,
            'writer': writer_instance.member_name
        }

        return render(request, 'funding_donation/donation__001/_T001.html', context)
