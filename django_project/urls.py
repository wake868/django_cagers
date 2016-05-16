from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'articles.views.index', name='index'),
    url(r'^articles/', include('articles.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
