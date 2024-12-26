from typing import Dict, List
from weather_and_activities_api.services.google_maps_service import GoogleMapsService
from weather_and_activities_api.services.open_ai_service import OpenAIService
from weather_and_activities_api.services.tomorrow_weather_service import TomorrowWeatherService


class ActivitiesComponent:
    def get_activities_suggestions(self, location: str) -> List[str]:
        """
        Get activities suggestions for a location.

        Args:
            location: Location string

        Returns:
            List of activity suggestions

        Raises:
            GeocodingException: If geocoding request fails
            TomorrowWeatherServiceException: If weather forecast request fails
            OpenAIServiceException: If OpenAI API request fails
        """
        latitude, longitude, formatted_address = GoogleMapsService().geocode_location(location)

        weather_context = self._get_weather_context(
            latitude=latitude,
            longitude=longitude
        )

        openai_service = OpenAIService()
        activities = openai_service.get_activity_suggestions(
            location_context=formatted_address,
            weather_context=weather_context
        )

        return activities

    def _get_weather_context(self, latitude: float, longitude: float) -> str:
        """
        Get 3 days weather forecast for a location and format it as a string to be used as context for OpenAI.

        Args:
            latitude: Latitude of the location
            longitude: Longitude of the location

        Returns:
            Weather forecast context string

        Raises:
            TomorrowWeatherServiceException: If weather forecast request fails
        """
        weather_service = TomorrowWeatherService()
        forecast_data = weather_service.get_weather_forecast_by_day(
            latitude=latitude,
            longitude=longitude
        )

        weather_info = "\n".join([
            f"Day {i + 1}: Average temperature {day['values']['temperatureAvg']}°C"
            for i, day in enumerate(forecast_data[:3])
        ])

        return weather_info
