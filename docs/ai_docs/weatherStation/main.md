# Documentation for src/weatherStation/main.py

# Python Documentation for Weather Prediction Script

## Program Overview

The provided script is designed to perform weather prediction using Ridge regression. It loads weather data from a MySQL database, processes it, and runs multiple regression tests to find the best hyperparameters for predicting weather conditions for different hours ahead. The script uses multiprocessing to load data concurrently and evaluate different alpha values for Ridge regression.

## Table of Contents

- [Function 1: `load_data`](#function-1-load_data)
    - Description: Loads weather data for a specified hour ahead.
    - Parameters: `hours`, `step`, `offset`, `num`, `total_workers`, `queue`, `target`
    - Returns: None

- [Function 2: `create_predictions_test`](#function-2-create_predictions_test)
    - Description: Creates predictions for a given target using Ridge regression and evaluates the model.
    - Parameters: `predictors`, `core_weather`, `target`, `alpha`
    - Returns: `error`, `combined`

- [Function 3: `run_all_tests`](#function-3-run_all_tests)
    - Description: Runs all tests for different hours ahead and alpha values to find the best hyperparameters.
    - Parameters: `predictors`, `target`, `hours`, `step`, `workers`, `alpha_min`, `alpha_max`, `alpha_step`
    - Returns: None

## Detailed Function Descriptions

### Function 1: `load_data`

**Description:** Loads weather data for a specified hour ahead from the MySQL database and puts it into a queue.

**Parameters:**
- `hours` (int): The total number of hours ahead to load data for.
- `step` (int): The step size for loading data.
- `offset` (int): The offset for loading data.
- `num` (int): The worker number.
- `total_workers` (int): The total number of workers.
- `queue` (multiprocessing.Queue): The queue to put the loaded data into.
- `target` (str): The target column name format.

**Returns:** None

**Example Usage:**

```python
queue = multiprocessing.Queue()
load_data(168, 1, 0, 0, 15, queue, "temp_{}h_ahead")
```

### Function 2: `create_predictions_test`

**Description:** Creates predictions for a given target using Ridge regression and evaluates the model by calculating the mean squared error.

**Parameters:**
- `predictors` (list): The list of predictor column names.
- `core_weather` (pd.DataFrame): The DataFrame containing the core weather data.
- `target` (str): The target column name.
- `alpha` (float, optional): The alpha value for Ridge regression. Default is 0.5.

**Returns:**
- `error` (float): The mean squared error of the predictions.
- `combined` (pd.DataFrame): The DataFrame containing the actual and predicted values.

**Example Usage:**

```python
predictors = ["temp", "humidity"]
core_weather = pd.read_csv("core_weather.csv", index_col="date")
target = "temp_1h_ahead"
error, combined = create_predictions_test(predictors, core_weather, target)
```

### Function 3: `run_all_tests`

**Description:** Runs all tests for different hours ahead and alpha values to find the best hyperparameters for Ridge regression. It loads data concurrently using multiprocessing and evaluates the model for each combination of hour and alpha value.

**Parameters:**
- `predictors` (list): The list of predictor column names.
- `target` (str): The target column name format.
- `hours` (int, optional): The total number of hours ahead to test. Default is 168.
- `step` (int, optional): The step size for testing. Default is 1.
- `workers` (int, optional): The number of workers for loading data. Default is 15.
- `alpha_min` (float, optional): The minimum alpha value for testing. Default is 0.1.
- `alpha_max` (float, optional): The maximum alpha value for testing. Default is 1.
- `alpha_step` (float, optional): The step size for alpha values. Default is 0.1.

**Returns:** None

**Example Usage:**

```python
predictors = ["temp", "humidity"]
target = "temp_{}h_ahead"
run_all_tests(predictors, target)
```

## Example Usage

Here is an example of how to use the script to run all tests with specific predictors and target:

```python
if __name__ == "__