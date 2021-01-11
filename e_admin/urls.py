from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import AdminKandidatView, PemilihView, ALLUpdateView, DashboardView

app_name = 'e_admin'

urlpatterns = [
    path('update/<str:nama>/<int:id>', ALLUpdateView.as_view(), name='update'),
    path('pemilih/', PemilihView.as_view(), name='pemilih'),
    path('kandidat/', AdminKandidatView.as_view(), name='list'),
    path('', DashboardView.as_view(), name='dashboard'),
]
