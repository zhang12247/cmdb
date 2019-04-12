from django.conf.urls import include, url
from assets import views
from django.urls import path
from django.urls import re_path

app_name = 'assets'
urlpatterns = [path(r'report/', views.report, name='report'),
               path(r'dashboard/', views.dashboard, name='dashboard'),
               path(r'index/', views.index, name='index'),
               re_path(r'^detail/(?P<asset_id>[0-9]+)/$', views.detail, name='detail'),
               re_path(r'^$', views.dashboard),
               ]
