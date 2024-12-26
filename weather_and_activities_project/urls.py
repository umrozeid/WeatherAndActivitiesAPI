from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers

from weather_and_activities_api.views.activities_suggestions_controller import ActivitiesSuggestionsController
from weather_and_activities_api.views.weather_forecast_controller import WeatherForecastController

router = routers.SimpleRouter()
router.register(r'weather/forecast', WeatherForecastController, basename='weather-forecast')
router.register(r'activities/suggestions', ActivitiesSuggestionsController, basename='activities-suggestions')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
urlpatterns += router.urls
