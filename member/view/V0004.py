from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class AdminRead(View):

    def get(self, request, id, *args, **kwargs):
        admins = Member.objects.get(id=id)
        context = {

            'admins': admins
        }
        return render(request, 'admin/admin__002/_T002.html')
