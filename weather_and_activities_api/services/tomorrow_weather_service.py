from typing import Dict, List

import requests
from django.conf import settings

from weather_and_activities_api.exceptions import TomorrowWeatherServiceException


class TomorrowWeatherService:
    __BASE_URL = settings.TOMORROW_API
    __API_VERSION = "v4"
    __WEATHER_FORECAST_API = f"{__BASE_URL}/{__API_VERSION}/weather/forecast"

    def __handle_response(self, response: requests.Response) -> Dict:
        """
        Handle Tomorrow Weather APIs response

        Args:
            response: API response object
        Returns:
            Dict containing the response payload
        Raises:
            TomorrowWeatherServiceException: If the API request fails
        """
        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            response_data = response.content.decode()

        if response.status_code != 200:
            raise TomorrowWeatherServiceException(response_data)

        return response_data

    def get_weather_forecast_by_day(self, latitude: float, longitude: float) -> List[Dict]:
        """
        Get weather forecast by day

        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
        Returns:
            List of daily weather forecasts
        Raises:
            TomorrowWeatherServiceException: If the API request fails
        """
        url_path = self.__WEATHER_FORECAST_API
        query_params = {
            "location": f"{latitude}, {longitude}",
            "units": "metric",
            "timesteps": "1d",
            "apikey": settings.TOMORROW_API_KEY
        }

        request_handler = requests.Session()

        response = request_handler.get(url=url_path, params=query_params)

        return self.__handle_response(response=response)["timelines"]["daily"]
