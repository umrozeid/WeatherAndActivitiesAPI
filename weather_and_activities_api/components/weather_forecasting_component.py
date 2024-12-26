from typing import List, Dict
from datetime import datetime

from weather_and_activities_api.services.google_maps_service import GoogleMapsService
from weather_and_activities_api.services.tomorrow_weather_service import TomorrowWeatherService


class WeatherForecastingComponent:
    def get_three_day_forecast(self, location: str) -> List[Dict]:
        """
        Get weather forecast for next 3 days for a given location.

        Args:
            location: String representing the location

        Returns:
            List of dicts containing weather forecast for 3 days with format:
            [
                {
                    "date": "2024-12-25",
                    "temperature_avg": -3.44,
                    "temperature_min": -6.13,
                    "temperature_max": -1.13
                },
                ...
            ]

        Raises:
            GeocodingException: If geocoding request fails
            TomorrowWeatherServiceException: If weather forecast request fails
        """
        latitude, longitude = GoogleMapsService().geocode_location(location)

        forecast_data = TomorrowWeatherService().get_weather_forecast_by_day(
            latitude=latitude,
            longitude=longitude
        )

        processed_forecast = []
        for day in forecast_data[:3]:
            date_obj = datetime.strptime(day["time"], "%Y-%m-%dT%H:%M:%SZ")
            processed_forecast.append({
                "date": date_obj.date().isoformat(),
                "temperature_avg": day["values"]["temperatureAvg"],
                "temperature_min": day["values"]["temperatureMin"],
                "temperature_max": day["values"]["temperatureMax"]
            })
        return processed_forecast
