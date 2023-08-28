from django.shortcuts import render
from django.views import View

from member.models import Notice


class NoticeView(View):
    def get(self, request, *args, **kwargs):

        notices = Notice.objects.all().order_by('-update_date')[:5]
        noticesDon = Notice.objects.filter(notice_title__contains='기부')

        context = dict(notices=notices, noticesDon=noticesDon)
        return render(request, 'notice/notice__001/_T001.html', context)



