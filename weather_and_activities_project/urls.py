from rest_framework import routers

from weather_and_activities_api.views.weather_forecast_controller import WeatherForecastController

router = routers.SimpleRouter()
router.register(r'weather/forecast', WeatherForecastController, basename='weather-forecast')

urlpatterns = router.urls
