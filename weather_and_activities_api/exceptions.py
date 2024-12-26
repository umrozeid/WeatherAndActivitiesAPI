from rest_framework import status
from rest_framework.exceptions import APIException


class TomorrowWeatherServiceException(APIException):
    status_code = status.HTTP_424_FAILED_DEPENDENCY
    default_detail = "Tomorrow Weather service has an issue"
    code = "TOMORROW_WEATHER_SERVICE_EXCEPTION"

    def __init__(self, message=None):
        if not message:
            message = self.default_detail

        super(TomorrowWeatherServiceException, self).__init__(detail=message, code=self.code)


class GoogleMapsGeocodingException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Encountered an issue while geocoding"
    code = "GOOGLE_MAPS_GEOCODING_EXCEPTION"

    def __init__(self, message=None, status_code=None):
        if not message:
            message = self.default_detail

        if status_code:
            self.status_code = status_code

        super(GoogleMapsGeocodingException, self).__init__(detail=message, code=self.code)
