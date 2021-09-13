from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.recurrent import LSTM
import time

def build_model(layers):
    model = Sequential() #for sequential data

    model.add(LSTM(   #first layer of LSTM
        units=layers[1],
        input_dim = layers[0],
        return_sequences = True))

    model.add(Dropout(0.2)) #prevents overfitting

    model.add(LSTM( #second LTSM layer
        layers[2],
        return_sequences = False))

    model.add(Dense(        #extract data
        units= layers[3]))

    model.add(Activation('linear'))  #applies linear unit activation function

    start = time.time()
    model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy']) #compiles model
    print('Compilation time :  ')
    print(time.time() - start)
    return model

