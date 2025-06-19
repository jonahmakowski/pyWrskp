# Documentation for src/weatherStation/raspberrypi3_script.py

# Python Documentation for Weather Station Script

## Program Overview

This script is designed to read temperature and humidity data from a DHT11 sensor connected to a Raspberry Pi. The data is collected every two minutes and stored in a MySQL database. The script uses the `adafruit_dht` library to interface with the DHT11 sensor and `sqlalchemy` to interact with the MySQL database.

## Table of Contents

* [Function 1](#function-1)
    * Description: This script continuously reads sensor data every two minutes and stores it in a MySQL database.
    * Parameters: None
    * Returns: None

## Detailed Function Descriptions

### Function 1

**Description:** This script continuously reads sensor data every two minutes and stores it in a MySQL database.

**Parameters:**
    * None

**Returns:**
    * None

## Example Usage

Below is an example of how to use the script. This script is intended to be run on a Raspberry Pi with a DHT11 sensor connected to GPIO27.

```python
import board
import adafruit_dht
from time import sleep
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Initialize the DHT11 sensor on GPIO27
dht_device = adafruit_dht.DHT11(board.D17)

# Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine("mysql://root:pd_goes_here@192.168.86.2:3306/weather_station")

last_minute = None
skip_wait = False

try:
    while True:
        try:
            # Wait until the current minute is even and not the same as the last minute
            while (
                datetime.now().minute % 2 != 0 or datetime.now().minute == last_minute
            ) or skip_wait:
                sleep(0.1)
            print("Reading sensor data...")
            skip_wait = False
            last_minute = datetime.now().minute

            # Read temperature and humidity from the sensor
            temp = dht_device.temperature
            humidity = dht_device.humidity
            now = datetime.now()

            # Create a DataFrame with the current sensor data
            current_row = pd.DataFrame(
                [[now, temp, humidity]], columns=["time", "temperature", "humidity"]
            )

            # Append the DataFrame to the 'live_data' table in the MySQL database
            current_row.to_sql("live_data", engine, if_exists="append", index=False)

            # Print the current sensor data
            print(now, temp, humidity)
        except RuntimeError as e:
            skip_wait = True
except KeyboardInterrupt:
    dht_device.exit()
```

## Notes

* Ensure that the DHT11 sensor is properly connected to the Raspberry Pi.
* Replace `pd_goes_here` with the actual password for the MySQL database.
* Make sure the MySQL database `weather_station` exists and has a table `live_data` with columns `time`, `temperature`, and `humidity`.
* This script is intended to run continuously until interrupted by the user (e.g., by pressing `Ctrl+C`).