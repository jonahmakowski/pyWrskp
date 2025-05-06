from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import pandas as pd
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
import multiprocessing
from pyWrkspPackage import json_write_file, list_to_str
load_dotenv()

engine = create_engine(f"mysql://root:{getenv('MYSQL_PASSWORD')}@192.168.86.2:3306/weather_station")

def load_data(hours, step, offset, num, total_workers, queue, target):
    for hour in range(1 + offset, hours + 1, step + total_workers - 1):
        print(f'[Data Loader {num}] Loading {hour}h ahead data')
        hour_ahead = pd.read_sql(f'SELECT date, {target.format(hour)} FROM combined_data', engine, index_col='date')
        queue.put((hour, hour_ahead))

def create_predictions_test(predictors, core_weather, target, alpha=0.5):
    reg = Ridge(alpha=alpha)
    train = core_weather.loc[:"2020-12-31"]
    test = core_weather.loc["2021-01-01":]

    reg.fit(train[predictors], train[target])
    predictions = reg.predict(test[predictors])

    error = mean_squared_error(test[target], predictions)
    
    combined = pd.concat([test[target], pd.Series(predictions, index=test.index)], axis=1)
    combined.columns = ["actual", "predictions"]
    return error, combined

def run_all_tests(predictors, target, hours=168, step=1, workers=15, alpha_min=0.1, alpha_max=1, alpha_step=0.1):
    errors = [[0 for _ in range(hours)] for _ in range(int(alpha_min*100), int(alpha_max*100), int(alpha_step*100))]
    threads = []
    queue = multiprocessing.Queue()

    for i in range(workers):
        thread = multiprocessing.Process(target=load_data, args=(hours, step, step * i, i, workers, queue))
        thread.start()
        threads.append(thread)
    
    print('[Main] Started Data Loader Thread')
    print('[Main] Loading Base Data')
    core_weather = pd.read_sql(f'SELECT {list_to_str(predictors, sep=', ')} FROM combined_data', engine, index_col='date')
    print('[Main] Loaded Base Data')
    
    hourly_data = {}
    for hour in range(1, hours + 1, step):
        print(f'[Main] {hour}h ahead data')
        
        have_data = False
        while not have_data:
            if hour in hourly_data:
                hour_ahead = hourly_data.pop(hour)
                have_data = True
            else:
                try:
                    loaded_hour, hour_ahead = queue.get(timeout=1)
                    hourly_data[loaded_hour] = hour_ahead
                except:
                    pass
        
        print(f'\t[Main] Loaded {hour}h ahead data')
        for error_index, alpha in enumerate(range(int(alpha_min*100), int(alpha_max*100), int(alpha_step*100))):
            alpha /= 100
            print(f'\t[Main] Testing with alpha {alpha}')
            core_weather_with_hour_ahead = core_weather.copy()
            core_weather_with_hour_ahead[target.format(hour)] = hour_ahead[target.format(hour)]
            target = target.format(hour)
            error, combined = create_predictions_test(predictors, core_weather_with_hour_ahead, target)
            errors[error_index][hour-1] += error
            print(f"\t\t[Main] Error: {error} with alpha {alpha}")
    
    for thread in threads:
        thread.join()
    
    best_per_hour = [1000 for _ in range(0, hours, step)]
    best_alpha_per_hour = [0 for _ in range(0, hours, step)]

    for error_index, alpha in enumerate(range(alpha_min, alpha_max, alpha_step)):
        for hour, _ in enumerate(best_per_hour):
            if errors[error_index][hour] < best_per_hour[hour]:
                best_per_hour[hour] = errors[error_index][hour]
                best_alpha_per_hour[hour] = alpha

    print(f'Average Error: {sum(best_per_hour) / len(best_per_hour)}')
    json_write_file('best_error_per_hour.json', best_per_hour)
    json_write_file('best_alpha_per_hour.json', best_alpha_per_hour)

if __name__ == "__main__":
    run_all_tests([])
