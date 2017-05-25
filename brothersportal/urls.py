from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^brothers/$', views.BrotherListView.as_view(), name='brothers'),
    url(r'^brother/(?P<pk>\d+)$', views.BrotherDetailView.as_view(), name='brother-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

