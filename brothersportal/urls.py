from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.portal, name='portal'),
    url(r'^brothers/$', views.all_brothers, name='brothers'),
    url(r'^brothers/actives$', views.all_actives, name='actives'),
    url(r'^brothers/alumni$', views.all_alumni, name='alumni'),
    url(r'^brother/(?P<pk>\d+)$', views.BrotherDetailView.as_view(), name='brother-detail'),
    url(r'^search/$', views.search_form, name='search-brothers'),
    url(r'^search/results/$', views.searchresults, name='search-results'),
    url(r'^export/csv/$', views.export_data_csv, name='export_data_csv'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

