from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Date,
    Integer,
    Float,
    MetaData,
    text
)


engine = create_engine("sqlite:///weather.db")

metadata = MetaData()


Pune_weather = Table(
    "Pune_weather",
    metadata,

    Column(
        "date",
        Date,
        primary_key=True
    ),

    Column(
        "hour",
        Integer,
        primary_key=True
    ),

    Column(
        "temperature_2m_c",
        Float
    ),

    Column(
        "relative_humidity_2m_pct",
        Float
    ),

    Column(
        "wind_speed_10m_kmh",
        Float
    ),

    Column(
        "rain_mm",
        Float
    )
)


def create_table():

    metadata.create_all(engine)


def load_weather_data(df):

    records = df.to_dict(orient="records")

    try:

        with engine.begin() as conn:

            for record in records:

                conn.execute(
                    text("""
                        INSERT OR IGNORE INTO Pune_weather
                        (
                            date,
                            hour,
                            temperature_2m_c,
                            relative_humidity_2m_pct,
                            wind_speed_10m_kmh,
                            rain_mm
                        )
                        VALUES
                        (
                            :date,
                            :hour,
                            :temperature_2m_c,
                            :relative_humidity_2m_pct,
                            :wind_speed_10m_kmh,
                            :rain_mm
                        )
                    """),
                    record
                )

        print("Weather data loaded successfully.")

    except Exception as e:

        raise RuntimeError(
            f"Database loading failed: {e}"
        )