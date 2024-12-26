from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

from weather_and_activities_api.components.activities_component import ActivitiesComponent


class ActivitiesSuggestionsController(ViewSet):
    @extend_schema(
        summary="Get activity suggestions",
        description="Retrieve suggested activities for a location taking into account the weather forecast",
        parameters=[
            OpenApiParameter(
                name="location",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Location string (e.g., 'San Francisco' or '90001')"
            ),
        ],
        responses={
            200: OpenApiResponse(
                description="Successfully retrieved activity suggestions",
                response={
                    "type": "object",
                    "properties": {
                        "activities_suggestions": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    }
                }
            )
        }
    )
    def list(self, request):
        """
        Retrieve suggested activities for a location taking into account the weather forecast

        Returns:
            Response: Array of suggested activities:
                [
                    "Visit Golden Gate Park",
                    "Take a cable car ride",
                    ...
                ]
        """
        location = request.query_params.get('location')
        if not location or not location.strip():
            return Response(
                {"error": "Location parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        activities_suggestions = ActivitiesComponent().get_activities_suggestions(
            location=location.strip()
        )
        return Response({"activities_suggestions": activities_suggestions})
