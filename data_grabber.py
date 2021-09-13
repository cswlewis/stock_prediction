import yfinance as yf
import numpy as np
import pandas as pd
import datetime

def get_stock_prices(stock_name): #returns stock data [Open, High, Low, Close]
    data = yf.Ticker(stock_name) #grab data from Yahoo finance
    df = data.history(period='max')
    column_names = ['Open', 'High', 'Low', 'Close']
    df = pd.DataFrame(df, columns=column_names)
    return df

def store_data(stock_name): #Saves data for later consideration
    today = datetime.date.today()
    file_name = stock_name + "_stock_%s.csv" %today
    data = get_stock_prices(stock_name)
    data.to_csv(file_name)


def data_loader(stock_name, seq_len, testing_proportion, normalise_num): #loads data in form required for LSTM
    data = get_stock_prices(stock_name)

    num_features = len(data.columns) #number of variables to analyse

    seq_len = seq_len + 1 #sequence of previous values for model to consider

    result = []
    data = data/normalise_num #normalises data between [0, 1]


    for i in range(len(data) - seq_len):
        result.append(data[i: i +seq_len])

    result = np.array(result)

    num_training_variables = round(testing_proportion * result.shape[0])
    train = result[:int(num_training_variables), :]

    #Set up training and testing data
    x_train = train[:, :-1]
    y_train = train[:, -1]
    x_test = result[int(num_training_variables):, :-1][:, :-1]
    y_test = result[int(num_training_variables):, -1][:, -1]

    #reshape data to fit model
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], num_features))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], num_features))

    return [x_train, y_train, x_test, y_test]



