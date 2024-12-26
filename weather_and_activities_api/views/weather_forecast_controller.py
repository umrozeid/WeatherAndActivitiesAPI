from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from weather_and_activities_api.components.weather_forecasting_component import WeatherForecastingComponent


class WeatherForecastController(ViewSet):
    @extend_schema(
        summary="Get weather forecast for 3 days",
        description="Retrieve the weather forecast for 3 days for a specified location",
        parameters=[
            OpenApiParameter(
                name="location",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Location string (e.g., 'San Francisco' or '90001')"
            ),
        ]
    )
    def list(self, request):
        """
        Retrieve the weather forecast for 3 days for a specified location

        Returns:
            Response: Array containing weather forecast:
                [
                    {
                        "date": "2024-12-25",
                        "temperature_avg": 20.5,
                        "temperature_min": 15.0,
                        "temperature_max": 25.0
                    },
                    ...
                ]
        """

        location = request.query_params.get('location')
        if not location or not location.strip():
            return Response({"error": "Location parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        weather_forecast = WeatherForecastingComponent().get_three_day_forecast(
            location=location.strip()
        )
        return Response({"weather_forecast": weather_forecast})
