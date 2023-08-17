from django.urls import path
from django.views.generic import TemplateView

app_name = 'member'



urlpatterns = [
    path('', TemplateView.as_view(template_name='base/__base__.html'), name='success'),
 ]

