# Name: Senhe Hao
# Assignment: Lab 10 part 4
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Main function
def main():
    # Reads in data
    input_file = open("WeatherDataWindows.csv", "r")
    days = input_file.readlines()
    del days[0]
    # values lists
    avg_temp = []
    avg_pres = []
    dates = []
    # for loop to get values
    for day in days:
        avg_temp.append(day[2])
        avg_pres.append(day[11])
        dates.append(day[0])
    # the plot
    plot1, plot2 = plt.subplots()
    color = 'tab:green'
    plt.title('Average temperatures and pressures')
    plot1.set_xlabel('Date')
    plot1.set_ylabel('Average temperature (F)', color=color)
    plot1.plot(avg_temp)
    plot1.tick_params(axis='y')
    plot2 = plot1.twinx()
    color = 'tab:red'
    plot2.set_ylabel('Average Pressure (mmHg)')
    plot2.plot(avg_pres, color=color)
    plot2.tick_params(axis='y')
    plot1.tight_layout()
    plt.show()


# If file is run call main
if __name__ == "__main__":
    main()
