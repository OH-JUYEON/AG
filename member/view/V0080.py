from django.shortcuts import render
from django.views import View

from member.models import Notice


class NoticeDetail(View):

    def get(self, request, id, *args, **kwargs):

        noticeCheck = Notice.objects.get(id=id)
        notices = Notice.objects.order_by('-create_date')
        noticeNames = Notice.objects.filter(notice_title__contains='강동')

        context = {
            'noticeCheck': noticeCheck,
            'notices': notices,
            'noticeNames': noticeNames,
        }
        return render(request, 'notice/notice__002/_T001.html', context)
