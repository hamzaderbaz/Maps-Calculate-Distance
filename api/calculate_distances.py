import requests
from django.conf import settings
import math

def get_coordinates(city):
    # Make a request to the geocoding service API (e.g., Google Maps Geocoding API)
    params = {
        'address': city,
        'key': settings.GOOGLE_MAPS_API_KEY
    }
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        if results:
            location = results[0].get('geometry', {}).get('location', {})
            latitude = location.get('lat')
            longitude = location.get('lng')
            return latitude, longitude

    return None



def calculate_distance(point1, point2):
    if point1 and point2:
        # Calculate the distance using the Haversine formula
        lat1, lon1 = point1
        lat2, lon2 = point2

        radius = 6371  # Earth's radius in kilometers

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = radius * c
        return distance

    return None










