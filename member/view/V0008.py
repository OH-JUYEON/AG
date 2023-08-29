from django.shortcuts import render, redirect
from django.views import View

from campaign.models import Campaign
from member.models import Member

# Create your views here.


# class Campaign_review:
#     def get(self, request, id, campaign_id=None, *args, **kwargs):
#
#         post = campaign_review.objects.get(id)
#         context = {
#
#
#             'posts': posts
#         }
#         return render(request, 'admin/admin__002/_T002.html')


from member.models import Member


class AdminRead(View):

    def get(self, request, *args, **kwargs):
        campaigns = Campaign.objects.all().order_by('-update_date')[:5]
        # admins = Member.objects.get(member_id=id)

        context = {

            'campaigns': campaigns,
            'admins': 'admins',

        }
        return render(request, 'admin/admin__006/_T006.html', context)
