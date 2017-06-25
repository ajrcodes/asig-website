from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/ZYChapterHistory', views.ZYChapterHistory, name='ZYChapterHistory'),
    url(r'^about/NationalsHistory', views.NationalsHistory, name='NationalsHistory'),

]

