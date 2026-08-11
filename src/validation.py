def validate_weather_data(df):

    expected_columns = [
        "date",
        "hour",
        "temperature_2m_c",
        "relative_humidity_2m_pct",
        "wind_speed_10m_kmh",
        "rain_mm"
    ]

    # Check required columns
    missing_columns = [
        column
        for column in expected_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

    # Check for null values
    if df[expected_columns].isna().any().any():
        raise ValueError(
            "Null values found in weather data."
        )

    # Check hour
    if ((df["hour"] < 0) | (df["hour"] > 23)).any():
        raise ValueError(
            "Invalid hour found. Hour must be between 0 and 23."
        )

    # Check humidity
    if (
        (df["relative_humidity_2m_pct"] < 0) |
        (df["relative_humidity_2m_pct"] > 100)
    ).any():
        raise ValueError(
            "Invalid humidity value found."
        )

    # Check rain
    if (df["rain_mm"] < 0).any():
        raise ValueError(
            "Invalid rain value found."
        )

    # Check wind speed
    if (df["wind_speed_10m_kmh"] < 0).any():
        raise ValueError(
            "Invalid wind speed value found."
        )

    # Check temperature
    if (
        (df["temperature_2m_c"] < -50) |
        (df["temperature_2m_c"] > 60)
    ).any():
        raise ValueError(
            "Invalid temperature value found."
        )

    # Check duplicate primary-key combination
    if df.duplicated(
        subset=["date", "hour"]
    ).any():
        raise ValueError(
            "Duplicate date-hour combination found."
        )

    print("Data validation passed.")