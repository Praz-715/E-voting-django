"""e_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView ,LogoutView
from .views import VotingLoginView, VotingHomeView , VotingHomeView2


urlpatterns = [
    path('votingout/<slug:slug>', TemplateView.as_view(template_name='voting/voting_logout.html'), name='votinglogout'),
    path('votinghome/<slug:slug>', VotingHomeView2.as_view(), name='votinghome'),
    path('voting/<slug:slug>', VotingLoginView.as_view(), name='votinglogin'), 
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TemplateView.as_view(template_name='base.html'), name=''),
    path('e-admin/', include('e_admin.urls', namespace='e_admin')),
    path('admin/', admin.site.urls),
]


# to upload file
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
