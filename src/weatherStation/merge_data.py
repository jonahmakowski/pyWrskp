from sqlalchemy import create_engine
import pandas as pd
from parse_data import send_to_db
from os import getenv
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(f"mysql://root:{getenv('MYSQL_PASSWORD')}@192.168.86.2:3306/weather_station")

def convert_bimin_to_hourly(df):
    df.index = pd.to_datetime(df.index)
    df.index = df.index.astype('datetime64[ns]')

    df_hourly = df.copy()
    df_hourly.index = df.index.floor('h')
    df_hourly = df_hourly[~df_hourly.index.duplicated(keep='first')]
    df_hourly.drop(columns=['temperature', 'humidity'], inplace=True)

    df_hourly['temperature'] = df.groupby(df.index.floor('h'))['temperature'].mean()
    df_hourly['humidity'] = df.groupby(df.index.floor('h'))['humidity'].mean()

    return df_hourly

def combine_data(ahead=168):
    df = pd.read_sql('historical_data', engine, index_col='date')
    df.dropna(inplace=True)

    df_bimin = pd.read_sql('live_data', engine, index_col='time')

    df_hourly = convert_bimin_to_hourly(df_bimin)
    df_hourly = send_to_db(df_hourly, engine, return_df=True)

    print('Sending historical data to DB')
    df.to_sql('combined_data', engine, if_exists='replace', index=True, index_label='date')
    print('Sending my data to DB')
    df_hourly.to_sql('combined_data', engine, if_exists='append', index=True, index_label='date')

    # Adding targets
    print('Adding Targets')
    combined_data = pd.read_sql('combined_data', engine, index_col='date')

    for i in range(1, ahead + 1):
        print(f'Adding {i}h ahead targets')
        combined_data[f'temperature_{i}h_ahead'] = combined_data['temperature'].shift(-i)
        combined_data[f'humidity_{i}h_ahead'] = combined_data['humidity'].shift(-i)
        combined_data = combined_data.copy()
    
    print('Dropping NaN values')
    combined_data.dropna(inplace=True)
    print('Sending combined data to DB')
    combined_data.to_sql('combined_data', engine, if_exists='replace', index=True, index_label='date')

if __name__ == "__main__":
    combine_data()
