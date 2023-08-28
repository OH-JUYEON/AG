"""
URL configuration for AG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from member.view import V0005, V0015, V0016, V0017



urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('campaign/', include('campaign.urls')),
    path('funding/', include('funding.urls')),
    path('donation/', include('donation.urls')),
    path('region/', include('region.urls')),
    path('pay/', include('pay.urls')),
    
    path("AG/",
        include(
            [
            path("", V0005.Main.as_view(), name="home"),
            path("login/", TemplateView.as_view(template_name='AG/login/_T001.html'), name="login"),
            path("logout/", V0017.Logout.as_view(), name="logout"),
            path("signup/", V0016.SignUp.as_view(), name="signup"),
            path('oauth/redirect/', V0015.Login.as_view(), name='redirect')
            ]
        ),
    ),

]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)