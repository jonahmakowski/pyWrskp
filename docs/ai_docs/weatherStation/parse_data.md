# Documentation for src/weatherStation/parse_data.py

# Python Script Documentation

## Program Overview

The provided script is designed to process weather data, add various predictors to the data, and send the processed data to a MySQL database. The script uses SQLAlchemy for database operations and Pandas for data manipulation.

## Table of Contents

- [send_to_db](#send_to_db)
  - Description: Processes the weather data, adds predictors, and sends the data to a MySQL database.
  - Parameters: List any input parameters required by the function.
  - Returns: Describe any output or return values produced by the function.

## Detailed Function Descriptions

### send_to_db

**Description:** This function processes the weather data, adds various predictors, and sends the data to a MySQL database.

**Parameters:**
- `df` (pandas.DataFrame): The input DataFrame containing weather data.
- `engine` (sqlalchemy.engine.base.Engine): The SQLAlchemy engine connected to the MySQL database.
- `out_table` (str, optional): The name of the table in the database where the data will be stored. Default is `None`.
- `return_df` (bool, optional): If `True`, the function will return the processed DataFrame instead of sending it to the database. Default is `False`.

**Returns:** If `return_df` is `True`, the function returns the processed DataFrame. Otherwise, it sends the data to the database and returns `None`.

## Example Usage

### Example Usage of `send_to_db`

```python
from sqlalchemy import create_engine
import pandas as pd
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql://root:{getenv('MYSQL_PASSWORD')}@192.168.86.2:3306/weather_station"
)

# Read weather data from CSV file
df = pd.read_csv(
    "historical-weather-data-hourly.csv",
    index_col=0,
    parse_dates=True,
    infer_datetime_format=True,
)

# Process the data and send it to the database
send_to_db(df, engine, "historical_data")
```

### Explanation

1. **Load Environment Variables**: The script uses the `dotenv` library to load environment variables from a `.env` file. This file should contain the `MYSQL_PASSWORD` variable.

2. **Create SQLAlchemy Engine**: The script creates a SQLAlchemy engine connected to the MySQL database using the `create_engine` function.

3. **Read Weather Data**: The script reads weather data from a CSV file named `historical-weather-data-hourly.csv` using the `pandas.read_csv` function. The `index_col=0` parameter specifies that the first column of the CSV file should be used as the index, and `parse_dates=True` and `infer_datetime_format=True` parameters are used to parse the index as datetime values.

4. **Process and Send Data**: The script calls the `send_to_db` function to process the weather data, add predictors, and send the data to the `historical_data` table in the MySQL database.