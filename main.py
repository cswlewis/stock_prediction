from data_grabber import store_data, data_loader
from model_builder import  build_model
from tools import plot_results, calculate_percentage_profit
import datetime




#Global variables
stock_shorthand = 'GOOG' #Used to find dataset on Yahoo finance
window = 5 #dimension of second LSTM layer
num_training_variables = 4 #number of parameters in code
normalise_num = 3000 #vary to normalise data

#grab data and save csv

store_data(stock_shorthand)

#populate data handlers
x_train, y_train, x_test, y_test = data_loader(stock_shorthand, 100, 0.95, normalise_num)
print('x_train, y_train, x_test, y_test shapes: ')
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

#build model with layers of dimension given in argument
model = build_model([4, window, 1, 1])

#fit model to the data
model.fit(
    x_train,
    y_train,
    batch_size=100,
    epochs=1,
    validation_split = 0.05)

#predict future values
prediction = model.predict(x_test)

#prints proportional profit if bought when model says the price is going/sold when model says is going down
print(calculate_percentage_profit(y_test, prediction, normalise_num))

#plots results
plot_results(y_test, prediction, stock_shorthand, normalise_num)