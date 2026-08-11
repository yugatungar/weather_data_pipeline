import pandas as pd


def transform_weather_data(data):

    df = pd.DataFrame(data["hourly"])

    df["time"] = pd.to_datetime(df["time"])

    df.rename(
        columns={
            "temperature_2m": "temperature_2m_c",
            "relative_humidity_2m": "relative_humidity_2m_pct",
            "wind_speed_10m": "wind_speed_10m_kmh",
            "rain": "rain_mm"
        },
        inplace=True
    )

    df.insert(
        0,
        "date",
        df["time"].dt.date
    )

    df.insert(
        1,
        "hour",
        df["time"].dt.hour
    )

    df.drop(
        columns=["time"],
        inplace=True
    )

    return df