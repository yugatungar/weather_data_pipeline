from api import fetch_weather_data
from transform import transform_weather_data
from validation import validate_weather_data
from database import create_table, load_weather_data


def main():

    print("Starting weather data pipeline...")

    # 1. Extract
    data = fetch_weather_data()

    # 2. Transform
    df = transform_weather_data(data)

    # 3. Validate
    validate_weather_data(df)

    # 4. Create database table
    create_table()

    # 5. Load into database
    load_weather_data(df)

    print("Weather data pipeline completed successfully.")


if __name__ == "__main__":
    main()