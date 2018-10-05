from django.db import models
from django.utils import timezone

class Frequency(models.Model):
    freq = models.IntegerField()

    class Meta:
        verbose_name_plural = 'frequencies'

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.freq)

class Country(models.Model):
    iso = models.CharField(max_length=3)
    full_name = models.CharField(max_length=32, null=True)

    class Meta:
        verbose_name_plural = 'countries'

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.full_name)

class Network(models.Model):
    network_name = models.CharField(max_length=64)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.network_name)

class Transmitter(models.Model):
    transmitter_name = models.CharField(max_length=64)
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
    details = models.TextField(blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.freq) + ": " + str(self.station_name) + " - " + str(self.transmitter)

class TextItem(models.Model):
    sortorder = models.IntegerField()
    heading = models.CharField(max_length=128)
    bodytext = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.heading
