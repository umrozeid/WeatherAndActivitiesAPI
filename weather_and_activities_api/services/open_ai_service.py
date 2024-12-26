from typing import List
from django.conf import settings
import openai
from weather_and_activities_api.exceptions import OpenAIServiceException


class OpenAIService:
    def __init__(self):
        openai.api_key = settings.OPEN_AI_API_KEY

    def get_activity_suggestions(self, location_context: str, weather_context: str) -> List[str]:
        """
        Get activity suggestions based on location and 3-day weather forecast using OpenAI.

        Args:
            location_context: Formatted location string
            weather_context: Formatted weather forecast string

        Returns:
            List of activity suggestions

        Raises:
            OpenAIServiceException: If the OpenAI API request fails
        """
        try:
            prompt = self._create_prompt(location_context, weather_context)

            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            activities = response.choices[0].message.content.split('\n')
            activities = [activity.strip().lstrip('123456789-. ')
                          for activity in activities if activity.strip()]

            return activities[:5]  # Return top 5 suggestions

        except Exception as e:
            raise OpenAIServiceException(f"Failed to get activity suggestions: {str(e)}")

    def _create_prompt(self, location_context: str, weather_context: str) -> str:
        """
        Create a prompt for the OpenAI API based on location and weather.
        """
        return (
            f"Suggest 5 activities for {location_context} based on the following 3-day weather forecast:\n"
            f"{weather_context}\n\n"
            "Focus on both outdoor and indoor activities appropriate for these conditions. "
            "Consider local attractions, cultural activities, and seasonal opportunities. "
            "Suggest activities that could be done across these days based on the weather patterns. "
            "Keep each suggestion concise and specific to the location and weather conditions."
            "The response should have exactly 5 lines. One suggestion per line."
        )