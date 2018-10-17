from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from markdownx.models import MarkdownxField

class Frequency(models.Model):
    freq = models.IntegerField()

    class Meta:
        verbose_name_plural = 'frequencies' # Stop the annoying 'frequencys' in the django admin!

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.freq)

class Country(models.Model):
    iso = models.CharField(max_length=3)
    full_name = models.CharField(max_length=32, null=True)
    country_slug = AutoSlugField(populate_from='iso')

    class Meta:
        verbose_name_plural = 'countries' # It's not 'countrys'

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.full_name)

class Network(models.Model):
    network_name = models.CharField(max_length=64)
    network_slug = AutoSlugField(populate_from='network_name')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.network_name)

class Transmitter(models.Model):
    transmitter_name = models.CharField(max_length=64)
    transmitter_slug = AutoSlugField(populate_from='transmitter_name')
    lat = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.transmitter_name)

class Station(models.Model):
    freq = models.ForeignKey('Frequency', on_delete=models.DO_NOTHING)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    station_name = models.ForeignKey('Network', on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=64, blank=True)
    transmitter = models.ForeignKey('Transmitter', on_delete=models.DO_NOTHING)
    power = models.DecimalField(max_digits=12, decimal_places=3)
    notes = models.CharField(max_length=256, blank=True)
    details = MarkdownxField(blank=True)

    def get_absolute_url(self):
        return "/detail/%i/" % self.pk

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.freq) + ": " + str(self.station_name) + " - " + str(self.transmitter)

class TextItem(models.Model): # These are the little posts on the sidebar
    sortorder = models.IntegerField()
    heading = models.CharField(max_length=128)
    bodytext = MarkdownxField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.heading

class Page(models.Model): # These are info pages like 'about' and 'links'
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=512)
    text = MarkdownxField()
    sortorder = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
