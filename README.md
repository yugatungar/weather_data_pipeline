# Automated API-to-Database Weather Pipeline

An automated Python data pipeline that extracts historical weather data from the Open-Meteo API, transforms and validates the data, and loads it into a SQLite database using SQLAlchemy.

## Architecture

Open-Meteo API
        ↓
Extraction
        ↓
Transformation
        ↓
Data Validation
        ↓
SQLite Database
        ↓
GitHub Actions

## Features

- Historical weather data extraction
- Automated daily execution
- API timeout handling
- API connection error handling
- API rate-limit handling
- Exponential retry mechanism
- Server error retry
- Data type conversion
- Null validation
- Range validation
- Duplicate detection
- 24-hour completeness validation
- SQL primary-key constraints
- Persistent SQLite database
- GitHub Actions automation

## Technologies

- Python
- Requests
- Pandas
- SQLAlchemy
- SQLite
- GitHub Actions

## Weather Variables

- Temperature
- Relative humidity
- Wind speed
- Rainfall

## Location

Pune, Maharashtra, India

## Database

The pipeline uses SQLite through SQLAlchemy.

The database file is:

weather.db

The primary key is:

(date, hour)

This prevents duplicate hourly records.

## Automation

GitHub Actions runs the pipeline daily.

The workflow:

1. Checks out the repository
2. Installs Python dependencies
3. Runs the pipeline
4. Updates weather.db
5. Commits the updated database back to GitHub