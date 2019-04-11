from django.conf.urls import include, url
from assets import views
from django.urls import path

app_name = 'assets'
urlpatterns = [path(r'report/', views.report, name='report'),]
