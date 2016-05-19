from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'compare.views.home', name='home'),
    url(r'^$', include('compareprice.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
