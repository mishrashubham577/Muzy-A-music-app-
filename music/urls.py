from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from muzy.settings import MEDIA_URL_TEMP, MEDIA_ROOT_TEMP, DEBUG

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_URL_TEMP,}),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL_TEMP, document_root=MEDIA_ROOT_TEMP)
