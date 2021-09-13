<h1> Stock Prediction Project </h1>

Uses Tensorflow and LSTM layers to predict future stock prices and then calculate the percentage return on an investment.

The investment would follow the predictions of the model whether the value of the stock goes up, or down each day and buying or shorting, respectively.

The model typically *lost* money in the long term due to the predictions being too heavily reliant on the previous days price. This behaviour is shown below.

![BTC-USD stock_2021-09-13_plot](https://user-images.githubusercontent.com/19304904/133164044-a0d8cb48-21bb-4d49-9d6d-e452acf4aa46.jpg)

It can be seen that the behaviour of the prediction appears to just lag the real data.

