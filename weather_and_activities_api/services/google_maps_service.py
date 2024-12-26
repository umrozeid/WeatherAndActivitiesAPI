from typing import Tuple
from django.conf import settings
import googlemaps
from googlemaps.exceptions import ApiError, Timeout, TransportError

from weather_and_activities_api.exceptions import GoogleMapsGeocodingException


class GoogleMapsService:
    def __init__(self):
        self.client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def geocode_location(self, location: str) -> Tuple[float, float]:
        """
        Geocode a location string to get its coordinates using Google Maps API.

        Args:
            location: Location string to geocode

        Returns:
            Tuple of (latitude, longitude) coordinates

        Raises:
            GeocodingException: If geocoding fails
        """
        try:
            result = self.client.geocode(location)

            if not result:
                raise GoogleMapsGeocodingException(f"Unable to geocode location: {location}")

            coordinates = result[0]['geometry']['location']
            return coordinates['lat'], coordinates['lng']

        except (ApiError, Timeout, TransportError):
            raise GoogleMapsGeocodingException(f"Geocoding failed for location: {location}")