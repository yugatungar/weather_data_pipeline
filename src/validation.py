def validate_weather_data(df):

    expected_columns = [
        "date",
        "hour",
        "temperature_2m_c",
        "relative_humidity_2m_pct",
        "wind_speed_10m_kmh",
        "rain_mm"
    ]

    # 1. Check required columns
    missing_columns = [
        column
        for column in expected_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

    # 2. Check record count
    if len(df) != 24:
        raise ValueError(
            f"Expected 24 hourly records, got {len(df)}."
        )

    # 3. Check null values
    if df[expected_columns].isna().any().any():

        null_columns = (
            df[expected_columns]
            .columns[
                df[expected_columns]
                .isna()
                .any()
            ]
            .tolist()
        )

        raise ValueError(
            f"Null values found in columns: "
            f"{', '.join(null_columns)}"
        )

    # 4. Check hour
    if ((df["hour"] < 0) | (df["hour"] > 23)).any():

        raise ValueError(
            "Invalid hour found. "
            "Hour must be between 0 and 23."
        )

    # 5. Check humidity
    if (
        (df["relative_humidity_2m_pct"] < 0) |
        (df["relative_humidity_2m_pct"] > 100)
    ).any():

        raise ValueError(
            "Invalid humidity value found. "
            "Humidity must be between 0 and 100."
        )

    # 6. Check rain
    if (df["rain_mm"] < 0).any():

        raise ValueError(
            "Invalid rain value found. "
            "Rain cannot be negative."
        )

    # 7. Check wind speed
    if (df["wind_speed_10m_kmh"] < 0).any():

        raise ValueError(
            "Invalid wind speed value found. "
            "Wind speed cannot be negative."
        )

    # 8. Check temperature
    if (
        (df["temperature_2m_c"] < -50) |
        (df["temperature_2m_c"] > 60)
    ).any():

        raise ValueError(
            "Invalid temperature value found. "
            "Temperature must be between -50°C and 60°C."
        )

    # 9. Check that data contains only one date
    if df["date"].nunique() != 1:

        raise ValueError(
            "Weather data contains multiple dates."
        )

    # 10. Check duplicate date-hour combinations
    if df.duplicated(
        subset=["date", "hour"]
    ).any():

        raise ValueError(
            "Duplicate date-hour combination found."
        )

    # 11. Check all 24 hours exist
    expected_hours = set(range(24))
    actual_hours = set(df["hour"])

    if actual_hours != expected_hours:

        missing_hours = sorted(
            expected_hours - actual_hours
        )

        raise ValueError(
            f"Missing hourly records: {missing_hours}"
        )

    print("Data validation passed.")