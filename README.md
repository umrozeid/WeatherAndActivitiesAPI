# Weather and Activities API

A Django REST API service that provides weather forecasts and activity suggestions based on location.

## Features

- Get 3-day weather forecasts for any location
- Get activity suggestions based on location and weather conditions
- Swagger documentation for easy API exploration
- Built with Django REST Framework

## APIs

The service exposes two main endpoints:

### Weather Forecast API
```
GET /weather/forecast/?location={location}
```
Returns a 3-day weather forecast for the specified location. The location can be a city name (e.g., "San Francisco") or postal code (e.g., "90001").

Example response:
```json
{
    "weather_forecast": [
        {
            "date": "2024-12-25",
            "temperature_avg": 20.5,
            "temperature_min": 15.0,
            "temperature_max": 25.0
        },
        ...
    ]
}
```

### Activities Suggestions API
```
GET /activities/suggestions/?location={location}
```
Returns a list of suggested activities for the specified location, taking into account the current weather conditions.

Example response:
```json
{
    "activities_suggestions": [
        "Visit Golden Gate Park",
        "Take a cable car ride",
        ...
    ]
}
```

## Setup

### Environment Variables

The following environment variables are required:

- `TOMORROW_API_KEY`: API key for Tomorrow.io weather service
- `GOOGLE_MAPS_API_KEY`: API key for Google Maps geocoding service
- `OPEN_AI_API_KEY`: API key for OpenAI service (used for activities suggestions)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd weather-and-activities-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables (create a .env file in the project root):
```
TOMORROW_API_KEY=your_tomorrow_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
OPEN_AI_API_KEY=your_openai_api_key
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

The API documentation is available through Swagger UI when the server is running:

- Swagger UI: `http://localhost:8000/api/docs/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## Suggested Improvements

1. Caching Layer
   - Implement Redis or Memcached for caching weather data and geocoding results
   - Cache weather forecasts with appropriate TTL to reduce API calls
   - Cache geocoding results for frequently requested locations

2. Rate Limiting
   - Add rate limiting for API endpoints to prevent abuse
   - Consider different rate limits for authenticated vs unauthenticated users

3. Monitoring and Observability
   - Implement comprehensive logging

4. Service Layer Abstraction
   - Create an abstract base class for weather services to allow easy switching between providers

5. Configuration Management
   - Add environment-specific configuration handling

6. Error Handling
   - Implement circuit breaker pattern for external service calls
   - Add detailed error logging and monitoring

7. Testing
   - Add unit tests for all components
   - Implement integration tests for external service interactions
