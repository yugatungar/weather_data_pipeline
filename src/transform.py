import pandas as pd


def transform_weather_data(data):

    if "hourly" not in data:
        raise ValueError(
            "API response does not contain hourly weather data."
        )

    hourly_data = data["hourly"]

    required_api_columns = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "rain"
    ]

    missing_columns = [
        column
        for column in required_api_columns
        if column not in hourly_data
    ]

    if missing_columns:
        raise ValueError(
            f"API response is missing columns: "
            f"{', '.join(missing_columns)}"
        )

    df = pd.DataFrame(hourly_data)

    # Convert timestamp
    df["time"] = pd.to_datetime(df["time"])

    # Rename API columns
    df.rename(
        columns={
            "temperature_2m": "temperature_2m_c",
            "relative_humidity_2m": "relative_humidity_2m_pct",
            "wind_speed_10m": "wind_speed_10m_kmh",
            "rain": "rain_mm"
        },
        inplace=True
    )

    # Extract date
    df.insert(
        0,
        "date",
        df["time"].dt.date
    )

    # Extract hour
    df.insert(
        1,
        "hour",
        df["time"].dt.hour
    )

    # Remove original timestamp
    df.drop(
        columns=["time"],
        inplace=True
    )

    # Convert weather columns to numeric
    numeric_columns = [
        "temperature_2m_c",
        "relative_humidity_2m_pct",
        "wind_speed_10m_kmh",
        "rain_mm"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    return df