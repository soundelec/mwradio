from django.contrib import admin
from .models import Frequency, Network, Transmitter, Station, TextItem, Page

class FrequencyAdmin(admin.ModelAdmin):
    ordering = ('freq',)
admin.site.register(Frequency, FrequencyAdmin)

#class CountryAdmin(admin.ModelAdmin):
#    ordering = ('full_name',)
#admin.site.register(Country, CountryAdmin)

class NetworkAdmin(admin.ModelAdmin):
    ordering = ('network_name',)
admin.site.register(Network, NetworkAdmin)

class TransmitterAdmin(admin.ModelAdmin):
    list_display = ('transmitter_name', 'lat', 'lon', 'iso', 'country_name')
    ordering = ('transmitter_name',)
admin.site.register(Transmitter, TransmitterAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display = ('freq', 'station_name', 'location', 'transmitter', 'power')
    list_display_links = ('station_name',)
    ordering = ('freq',)
admin.site.register(Station, StationAdmin)

class TextItemAdmin(admin.ModelAdmin):
    ordering = ('heading',)
admin.site.register (TextItem, TextItemAdmin)

class PageAdmin(admin.ModelAdmin):
    ordering = ('sortorder',)
admin.site.register (Page, PageAdmin)
