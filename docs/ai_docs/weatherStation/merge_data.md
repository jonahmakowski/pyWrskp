# Documentation for src/weatherStation/merge_data.py

# Weather Station Data Processing Script

This script is designed to process and combine weather station data from two different sources: historical data and live data. It converts live data from a 2-minute interval to an hourly interval, combines it with historical data, and adds future target values for temperature and humidity. The combined data is then stored in a MySQL database.

## Table of Contents

- [Function 1: convert_bimin_to_hourly](#function-1-convert_bimin_to_hourly)
  - Description: Converts live data from a 2-minute interval to an hourly interval.
  - Parameters: `df` (pandas DataFrame)
  - Returns: `df_hourly` (pandas DataFrame)

- [Function 2: combine_data](#function-2-combine_data)
  - Description: Combines historical and live data, adds future target values, and stores the combined data in the database.
  - Parameters: `ahead` (int, default=168)
  - Returns: None

## Detailed Function Descriptions

### Function 1: convert_bimin_to_hourly

**Description**: This function converts live data from a 2-minute interval to an hourly interval by averaging the temperature and humidity values for each hour.

**Parameters**:
- `df` (pandas DataFrame): The input DataFrame containing live data with a 2-minute interval.

**Returns**:
- `df_hourly` (pandas DataFrame): The output DataFrame with data converted to an hourly interval.

### Function 2: combine_data

**Description**: This function combines historical and live data, adds future target values for temperature and humidity, and stores the combined data in the database.

**Parameters**:
- `ahead` (int, default=168): The number of hours ahead to add target values for temperature and humidity.

**Returns**: None

## Example Usage

### Example Usage for convert_bimin_to_hourly

```python
import pandas as pd

# Sample live data DataFrame
data = {
    "temperature": [20, 21, 22, 23, 24],
    "humidity": [50, 55, 60, 65, 70]
}
index = pd.date_range(start="2023-01-01 00:00", periods=5, freq="2T")
df_live = pd.DataFrame(data, index=index)

# Convert live data to hourly interval
df_hourly = convert_bimin_to_hourly(df_live)
print(df_hourly)
```

### Example Usage for combine_data

```python
# Combine historical and live data, add future target values, and store in the database
combine_data(ahead=168)
```

## Detailed Code Explanation

### Database Connection

The script uses SQLAlchemy to connect to a MySQL database. The connection string is constructed using environment variables loaded from a `.env` file.

```python
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    f"mysql://root:{getenv('MYSQL_PASSWORD')}@192.168.86.2:3306/weather_station"
)
```

### Function: convert_bimin_to_hourly

This function converts live data from a 2-minute interval to an hourly interval by averaging the temperature and humidity values for each hour.

```python
def convert_bimin_to_hourly(df):
    df.index = pd.to_datetime(df.index)
    df.index = df.index.astype("datetime64[ns]")

    df_hourly = df.copy()
    df_hourly.index = df.index.floor("h")
    df_hourly = df_hourly[~df_hourly.index.duplicated(keep="first")]
    df_hourly.drop(columns=["temperature", "humidity"], inplace=True)

    df_hourly["temperature"] = df.groupby(df.index.floor("h"))["temperature"].mean()
    df_hourly["humidity"] = df.groupby(df.index.floor("h"))["humidity"].mean()

    return df_hourly
```

### Function: combine_data

This function combines historical and live data, adds future target values for temperature and humidity, and stores the combined data in the database.

```python
def combine_data(ahead=168):
    df = pd.read_sql("historical_data", engine, index_col="date")
    df.dropna(inplace=True)

    df_bimin = pd.read_sql("live_data", engine, index_col="time")

    df_hourly = convert_bimin_to_hourly(df_bimin)
    df_hourly = send_to_db(df_hourly, engine, return_df=True)

