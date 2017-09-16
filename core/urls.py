from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/zy-chapter-history', views.ZYChapterHistory, name='ZYChapterHistory'),
    url(r'^about/nationals-history', views.NationalsHistory, name='NationalsHistory'),
    url(r'^about/current-leadership', views.CurrentLeadership, name='CurrentLeadership'),
    url(r'^alumni', views.AlumniPage, name='AlumniPage'),
    url(r'^support', views.SupportPage, name='SupportPage'),
    url(r'^contact', views.ContactPage, name='ContactPage')
]
