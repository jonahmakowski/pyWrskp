from sqlalchemy import create_engine
import pandas as pd
import warnings
from os import getenv
from dotenv import load_dotenv

load_dotenv()

warnings.simplefilter(action='ignore', category=FutureWarning)

engine = create_engine(f"mysql://root:{getenv('MYSQL_PASSWORD')}@192.168.86.2:3306/weather_station")

def send_to_db(df, engine, out_table=None, return_df=False):
    df.index = pd.to_datetime(df.index)
    df.index = df.index.astype('datetime64[ns]')

    df = df.rename(columns={
        'temperature_2m (°C)': 'temperature',
        'relative_humidity_2m (%)': 'humidity'
    })

    # Add Predictors
    print('Adding predictors')
    df["monthly_avg"] = df["temperature"].groupby(df.index.month).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)
    df["day_avg"] = df["temperature"].groupby(df.index.day).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)
    df["day_of_year_avg"] = df["temperature"].groupby(df.index.day_of_year).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)
    
    df["monthly_avg_humidity"] = df["humidity"].groupby(df.index.month).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)
    df["day_avg_humidity"] = df["humidity"].groupby(df.index.day).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)
    df["day_of_year_avg_humidity"] = df["humidity"].groupby(df.index.day_of_year).apply(lambda x: x.expanding(1).mean()).reset_index(level=0, drop=True)

    ## Daily Data
    df['daily_high'] = df['temperature'].rolling(24).max()
    df['daily_low'] = df['temperature'].rolling(24).min()
    
    df['daily_high_humidity'] = df['humidity'].rolling(24).max()
    df['daily_low_humidity'] = df['humidity'].rolling(24).min()
    
    df['daily_min_max'] = df['daily_high'] - df['daily_low']
    df['daily_min_max_humidity'] = df['daily_high_humidity'] - df['daily_low_humidity']

    ## Yesterday's relative
    df['temperature_yesterday'] = df['temperature'].shift(24)
    df['humidity_yesterday'] = df['humidity'].shift(24)
    df['relative_temperature_yesterday'] = df['temperature'].shift(24) - df['temperature']
    df['relative_humidity_yesterday'] = df['humidity'].shift(24) - df['humidity']

    print('Sending to DB')
    if return_df:
        return df
    else:
        df.to_sql(out_table, engine, if_exists='replace', index=True, index_label='date')

if __name__ == "__main__":
    df = pd.read_csv('historical-weather-data-hourly.csv', index_col=0, parse_dates=True, infer_datetime_format=True)
    send_to_db(df, engine,'historical_data')
