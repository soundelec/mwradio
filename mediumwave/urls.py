from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',
    views.IndexView.as_view(),
    name="freq_list"
        ),
    url(r'^freq/$',
    views.IndexView.as_view(),
    name="freq_list"
        ),
    url(r'^station/$',
    views.StationList.as_view(),
    name="station_list"
        ),
    #url(r'^country/$',
    #views.CountryList.as_view(),
    #name="country_list"
    #    ),
    url(r'^lw/$',
    views.LWList.as_view(),
    name="freq_list"
        ),
    url(r'^freq/(?P<frequrl>[0-9]{3,4})/$',
    views.FreqView.as_view(),
    name="single_freq"
        ),
    url(r'^station/(?P<stnurl>.+)/$',
    views.StationView.as_view(),
    name="single_station"
        ),
    #url(r'^country/(?P<countryurl>.+)/$',
    #views.CountryView.as_view(),
    #name="single_country"
    #    ),
    url(r'^detail/(?P<pk>.+)/$',
    views.StationDetail.as_view(),
    name="station_detail"
        ),
    url(r'^page/(?P<slug>.+)/$',
    views.PageView.as_view(),
    name="page"
        ),
    url(r'^search/', include('haystack.urls')),
    url(r'^about/$', views.about, name='about'),
    url(r'^markdownx/', include('markdownx.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
