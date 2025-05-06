import board
import adafruit_dht
from time import sleep
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

dht_device = adafruit_dht.DHT11(board.D17)  # GPIO27
engine = create_engine("mysql://root:pd_goes_here@192.168.86.2:3306/weather_station")
last_minute = None
skip_wait = False

try:
    while True:
        try:
            while (datetime.now().minute % 2 != 0 or datetime.now().minute == last_minute) or skip_wait:
                sleep(0.1)
            print("Reading sensor data...")
            skip_wait = False
            last_minute = datetime.now().minute
            temp = dht_device.temperature
            humidity = dht_device.humidity
            now = datetime.now()
            current_row = pd.DataFrame([[now, temp, humidity]], columns=['time', 'temperature', 'humidity'])
            current_row.to_sql('live_data', engine, if_exists='append', index=False)
            print(now, temp, humidity)
        except RuntimeError as e:
            skip_wait = True
except KeyboardInterrupt:
    dht_device.exit()
