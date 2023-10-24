from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np
import pandas as pd

# File path to the Excel data
file_path = 'data-for-predicting-hr.xlsx'

# Dictionary to store cleaned DataFrames for each sheet
cleaned_dfs = {}

# Get the list of sheet names in the Excel file
with pd.ExcelFile(file_path) as xls:
    sheet_names = xls.sheet_names

# Iterate through each sheet and remove rows with missing values in the 'hr_mean' column
for sheet_name in sheet_names:
    # Load the sheet into a DataFrame
    sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Remove rows where 'hr_mean' is NaN
    cleaned_df = sheet_df.dropna(subset=['hr_mean'])

    # Store the cleaned DataFrame
    cleaned_dfs[sheet_name] = cleaned_df


# Function to train and evaluate ARIMA model
def train_and_evaluate_arima(y_train, y_test):
    model = ARIMA(y_train, order=(5,1,0))
    model_fit = model.fit()
    forecast_output = model_fit.forecast(steps=len(y_test))
    y_pred = forecast_output.values  # Use the Pandas Series values
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mae, mse, r2


# Function to train and evaluate LSTM model
def train_and_evaluate_lstm(X_train, X_test, y_train, y_test):
    X_train_reshaped = np.reshape(X_train.values, (X_train.shape[0], 1, X_train.shape[1]))
    X_test_reshaped = np.reshape(X_test.values, (X_test.shape[0], 1, X_test.shape[1]))
    model = Sequential()
    model.add(LSTM(50, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train_reshaped, y_train, epochs=50, batch_size=72, verbose=0)
    y_pred = model.predict(X_test_reshaped)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mae, mse, r2


# Loop through the cleaned DataFrames for each sheet
    # Inside your loop through cleaned DataFrames
for sheet_name, cleaned_df in cleaned_dfs.items():
    print(f"Processing sheet: {sheet_name}")

        # Filter to only numeric columns to avoid TensorFlow error
    X = cleaned_df.select_dtypes(include=[np.number]).drop(columns=['hr_mean'])
    y = cleaned_df['hr_mean']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize models
    # Initialize and fit models
    linear_model = LinearRegression().fit(X_train, y_train)
    rf_model = RandomForestRegressor(random_state=42).fit(X_train, y_train)
    gb_model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)

    # Make predictions
    linear_pred = linear_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)
    gb_pred = gb_model.predict(X_test)

    # Evaluate models
    linear_mae = mean_absolute_error(y_test, linear_pred)
    linear_mse = mean_squared_error(y_test, linear_pred)
    linear_r2 = r2_score(y_test, linear_pred)

    rf_mae = mean_absolute_error(y_test, rf_pred)
    rf_mse = mean_squared_error(y_test, rf_pred)
    rf_r2 = r2_score(y_test, rf_pred)

    gb_mae = mean_absolute_error(y_test, gb_pred)
    gb_mse = mean_squared_error(y_test, gb_pred)
    gb_r2 = r2_score(y_test, gb_pred)

    # Your existing code for training and evaluation of Linear Regression, Random Forest, and Gradient Boosting goes here

    # Train and evaluate ARIMA model
    arima_mae, arima_mse, arima_r2 = train_and_evaluate_arima(y_train.reset_index(drop=True),
                                                              y_test.reset_index(drop=True))

    # Train and evaluate LSTM model
    lstm_mae, lstm_mse, lstm_r2 = train_and_evaluate_lstm(X_train, X_test, y_train, y_test)

    # Compile all results
    results = {
        'Model': ['Linear Regression', 'Random Forest', 'Gradient Boosting', 'ARIMA', 'LSTM'],
        'MAE': [linear_mae, rf_mae, gb_mae, arima_mae, lstm_mae],
        'MSE': [linear_mse, rf_mse, gb_mse, arima_mse, lstm_mse],
        'R2': [linear_r2, rf_r2, gb_r2, arima_r2, lstm_r2]
    }

    results_df = pd.DataFrame(results)
    print("Results for sheet:", sheet_name)
    print(results_df)
    print("\n" + "=" * 50 + "\n")