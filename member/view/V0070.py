from django.shortcuts import render
from django.views import View


class Faq(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'faq/faq__001/_T001.html')