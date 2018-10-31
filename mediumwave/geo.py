# Take the latitude and longitude of a tx and get country info

import pycountry
from geopy.geocoders import Nominatim

def get_country(self, lat, lon, iso):
    geolocator = Nominatim(user_agent="mediumwave")
    if self.lat:
        lat = str(self.lat)
        lon = str(self.lon)
        latlon = lat + ", " + lon
        c = geolocator.reverse(latlon)
        cc = c.raw['address']['country_code']
        if cc=="xk": # special case for Kosovo
            countryiso = "KS"
        else:
            countryiso = cc.upper()
    else:
        countryiso = ""

    return countryiso

def get_country_name(self, lat, lon, country_name): # Yes, we are hard-coding in English country names
    geolocator = Nominatim(user_agent="mediumwave")
    if self.lat:
        lat = str(self.lat)
        lon = str(self.lon)
        latlon = lat + ", " + lon
        c = geolocator.reverse(latlon)
        cc = c.raw['address']['country_code']
        if cc=="xk": # special case for Kosovo
            cc = "KS"
        else:
            cc = cc.upper()
        country = pycountry.countries.get(alpha_2=cc)
        countryname = str(country.name)
    else:
        countryname = ""

    return countryname
