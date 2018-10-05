from django.shortcuts import render
from .models import Station, Network, Frequency, Country, Transmitter, TextItem
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.template import loader
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

class IndexView(ListView):
    context_object_name = 'freq_list'
    template_name = 'mw/freq_list.html'
    queryset = Station.objects.order_by('frequency__freq')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['stations'] = Station.objects.filter(freq__freq__gte=300).order_by('freq__freq', 'country__iso', 'station_name__network_name', '-power')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class StationList(ListView):
    context_object_name = 'station_list'
    template_name = 'mw/station_list.html'
    queryset = Station.objects.order_by('station_name__network_name')

    def get_context_data(self, **kwargs):
        context = super(StationList, self).get_context_data(**kwargs)
        context['stations'] = Station.objects.order_by('station_name__network_name', 'freq__freq', '-power')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class CountryList(ListView):
    context_object_name = 'country_list'
    template_name = 'mw/country_list.html'
    queryset = Country.objects.order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super(CountryList, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.order_by('full_name')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class LWList(ListView):
    context_object_name = 'freq_list'
    template_name = 'mw/freq_list.html'
    queryset = Station.objects.order_by('freq__freq')

    def get_context_data(self, **kwargs):
        context = super(LWList, self).get_context_data(**kwargs)
        context['stations'] = Station.objects.filter(freq__freq__lt=300).order_by('freq__freq', 'country__iso', 'station_name__network_name', '-power')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class FreqView(ListView):
    template_name = 'mw/single_freq.html'
    queryset = Station.objects.order_by('station_name__network_name')

    def get_context_data(self, **kwargs):
        freq_filter = str(self.kwargs['frequrl'])
        context = super(FreqView, self).get_context_data(**kwargs)
        context['station'] = Station.objects.filter(freq__freq=freq_filter).order_by('station_name__network_name')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class StationView(ListView):
    template_name = 'mw/single_station.html'
    queryset = Station.objects.order_by('station_name')

    def get_context_data(self, **kwargs):
        stn_filter = str(self.kwargs['stnurl'])
        context = super(StationView, self).get_context_data(**kwargs)
        #context['station'] = Station.objects.filter(station_name__network_name=stn_filter).order_by('freq__freq')
        context['station'] = Station.objects.filter(station_name__network_slug=stn_filter).order_by('freq__freq')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class CountryView(ListView):
    template_name = 'mw/single_country.html'
    queryset = Station.objects.order_by('country.full_name')

    def get_context_data(self, **kwargs):
        stn_filter = str(self.kwargs['countryurl'])
        context = super(CountryView, self).get_context_data(**kwargs)
        context['station'] = Station.objects.filter(country__full_name=stn_filter).order_by('freq__freq', 'station_name__network_name', '-power', 'country__full_name')
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

class StationDetail(DetailView):
    template_name = 'mw/station_detail.html'
    queryset = Station.objects.order_by('station_name')

    def get_context_data(self, **kwargs):
        stn_filter = self.kwargs['pk']
        context = super(DetailView, self).get_context_data(**kwargs)
        context['station'] = Station.objects.get(pk=self.kwargs.get('pk'))
        context['widgets'] = TextItem.objects.order_by('sortorder')
        return context

def about(request):
    return render(request,'mw/about.html')

# Search view
class StationSearchListView(ListView):
    template_name = 'mw/station_search.html'
    model = Station
    paginate_by = 10

    def get_queryset(self):
        qs = Station.objects.all()

        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            vector = SearchVector('station_name__network_name', 'transmitter__transmitter_name', 'location')
            qs = qs.annotate(search=vector).filter(search=query)
            qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        return qs
