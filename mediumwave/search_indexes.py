import datetime
from haystack import indexes
from mediumwave.models import Station


class StationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    station_name = indexes.CharField(model_attr='station_name__network_name')
    freq = indexes.IntegerField(model_attr='freq__freq')
    location = indexes.CharField(model_attr='location')
    transmitter = indexes.CharField(model_attr='transmitter__transmitter_name')

    def get_model(self):
        return Station

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()
