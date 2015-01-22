from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^car_extraction/opinion_target/$', 'web_platform.car_extraction.views.opinion_target'),
    url(r'^$', 'web_platform.car_extraction.views.opinion_target'),
    url(r'^analysis/segmentation/$', 'web_platform.analysis.views.segmentation'),
)
