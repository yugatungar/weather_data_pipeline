import time
import requests
from datetime import date, timedelta


URL = "https://historical-forecast-api.open-meteo.com/v1/forecast"

MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 2


def fetch_weather_data():

    # Get yesterday's date automatically
    yesterday = date.today() - timedelta(days=1)

    yesterday = yesterday.isoformat()

    params = {
        "latitude": 18.5204,
        "longitude": 73.8567,
        "timezone": "Asia/Kolkata",

        "start_date": yesterday,
        "end_date": yesterday,

        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "wind_speed_10m,"
            "rain"
        )
    }

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            print(
                f"Fetching weather data for {yesterday}..."
            )

            response = requests.get(
                URL,
                params=params,
                timeout=30
            )

            # API rate limit
            if response.status_code == 429:

                if attempt == MAX_RETRIES:
                    raise RuntimeError(
                        "API rate limit exceeded after maximum retries."
                    )

                delay = INITIAL_RETRY_DELAY * (2 ** (attempt - 1))

                print(
                    f"Rate limit reached. "
                    f"Retrying in {delay} seconds..."
                )

                time.sleep(delay)
                continue

            response.raise_for_status()

            print("Weather data fetched successfully.")

            return response.json()

        except requests.exceptions.Timeout:

            print(
                f"Request timed out. "
                f"Attempt {attempt}/{MAX_RETRIES}"
            )

        except requests.exceptions.ConnectionError:

            print(
                f"Connection error. "
                f"Attempt {attempt}/{MAX_RETRIES}"
            )

        except requests.exceptions.HTTPError as e:

            raise RuntimeError(
                f"HTTP error while calling weather API: {e}"
            )

        except requests.exceptions.RequestException as e:

            raise RuntimeError(
                f"Weather API request failed: {e}"
            )

        if attempt < MAX_RETRIES:

            delay = INITIAL_RETRY_DELAY * (2 ** (attempt - 1))

            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)

    raise RuntimeError(
        "Unable to fetch weather data after maximum retries."
    )