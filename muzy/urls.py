from django.conf.urls import include, url
from django.contrib import admin
from music import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'muzy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ]