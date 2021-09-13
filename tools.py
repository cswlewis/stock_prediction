import datetime
import matplotlib.pyplot as plt

def plot_results(real_data, predicted_data, stock_name, normalise_num):

    #plots real_data versus predicted_data

    fig = plt.figure()
    plt.plot(real_data * normalise_num, color='purple', label='Actual Values')
    plt.plot(predicted_data * normalise_num, color='blue', label='Predicted Values')
    plt.legend()
    plt.ylabel("Price[$]")
    plt.xlabel("Time[days]")

    today = datetime.date.today()
    plot_name = stock_name + ' stock_%s_plot.jpg' %today
    fig.savefig(plot_name) #saves plot
    plt.show()

def calculate_percentage_profit(real_data, predicted_data, normalise_num):

    #used to calculate profit given that a lump sum would be staked on models predictions
    #returns proportional profit/loss of original sum

    total_proportional_gain = 1
    real_data =real_data*normalise_num
    predicted_data = predicted_data * normalise_num
    for day in range(len(real_data)-1):
        if((predicted_data[day+1] > predicted_data[day]) & (real_data[day+1] > real_data[day])):
            total_proportional_gain = total_proportional_gain + total_proportional_gain*((real_data[day] -  real_data[day+1]) / real_data[day])

        elif((predicted_data[day+1] < predicted_data[day]) & (real_data[day+1] > real_data[day])):
            total_proportional_gain = total_proportional_gain + total_proportional_gain*((real_data[day] -  real_data[day+1]) / real_data[day])

        elif ((predicted_data[day+1] > predicted_data[day]) & (real_data[day+1] < real_data[day])):
            total_proportional_gain = total_proportional_gain + total_proportional_gain*((real_data[day] -  real_data[day+1]) / real_data[day])

        elif ((predicted_data[day+1] < predicted_data[day]) & (real_data[day+1] < real_data[day])):
            total_proportional_gain = total_proportional_gain + total_proportional_gain*((real_data[day] -  real_data[day+1]) / real_data[day])

        else:
            print('ERROR: Prices Identical.')
        if(total_proportional_gain < 0):
            print("You went broke!")
            break
        #print(day)
        #print(total_proportional_gain)


    proportional_gain_per_day = (total_proportional_gain-1)/(len(real_data)-1)

    return total_proportional_gain, len(real_data), proportional_gain_per_day





