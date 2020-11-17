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
    precipitations = []
    avg_dew_point = []
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    october = []
    nov = []
    dec = []
    # for loop to get values
    for day in days:
        entry = day.split(",")
        avg_temp.append(float(entry[2]))
        avg_pres.append(float(entry[11]))
        precipitations.append(float(entry[13]))
        avg_dew_point.append(float(entry[5]))
        dates.append(day[0])
        temp = entry[0].split("/")
        if int(temp[0]) == 1:
            jan.append(int(entry[2]))
        elif int(temp[0]) == 2:
            feb.append(int(entry[2]))
        elif int(temp[0]) == 3:
            mar.append(int(entry[2]))
        elif int(temp[0]) == 4:
            apr.append(int(entry[2]))
        elif int(temp[0]) == 5:
            may.append(int(entry[2]))
        elif int(temp[0]) == 6:
            jun.append(int(entry[2]))
        elif int(temp[0]) == 7:
            jul.append(int(entry[2]))
        elif int(temp[0]) == 8:
            aug.append(int(entry[2]))
        elif int(temp[0]) == 9:
            sep.append(int(entry[2]))
        elif int(temp[0]) == 10:
            october.append(int(entry[2]))
        elif int(temp[0]) == 11:
            nov.append(int(entry[2]))
        elif int(temp[0]) == 12:
            dec.append(int(entry[2]))
    # the plot for part 1
    fig, ax1 = plt.subplots()
    color = 'green'
    plt.title('Average temperatures and pressures')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Average temperature (F)')
    ax1.plot(avg_temp, color=color)
    ax1.legend(['Temperature'])
    ax1.tick_params(axis='y')
    ax2 = ax1.twinx()
    color = 'red'
    ax2.set_ylabel('Average Pressure (mmHg)')
    ax2.plot(avg_pres, color=color)
    ax2.legend(['Pressure'])
    ax2.tick_params(axis='y')
    fig.tight_layout()
    plt.show()
    # histogram for precipitation
    plt.hist(precipitations)
    plt.ylabel("number of days")
    plt.xlabel("precipitation amount in inches")
    plt.title("Precipitation histogram")
    plt.show()
    # Scatterplot for relationship between average temp and average dew point.
    plt.scatter(avg_temp, avg_dew_point)
    plt.xlabel("Average temperature in degrees F")
    plt.ylabel("Average dew point")
    plt.title("Average dew point vs average temperature")
    plt.show()
    # Bar graph
    categories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    values = [sum(jan)/len(jan), sum(feb)/len(feb), sum(mar)/len(mar), sum(apr)/len(apr), sum(may)/len(may), sum(jun)/len(jun), sum(jul)/len(jul), sum(aug)/len(aug), sum(sep)/len(sep), sum(october)/len(october), sum(nov)/len(nov), sum(dec)/len(dec)]
    highs = [max(jan), max(feb), max(mar), max(apr), max(may), max(jun), max(jul), max(aug), max(sep), max(october), max(nov), max(dec)]
    lows = [min(jan), min(feb), min(mar), min(apr), min(may), min(jun), min(jul), min(aug), min(sep), min(october),
             min(nov), min(dec)]
    plt.bar(categories, values)
    plt.errorbar(categories, highs, label='Error High')
    plt.errorbar(categories, lows, label='Error Low')
    plt.legend(loc='upper right')
    plt.ylabel('average temperature in F')
    plt.xlabel('Month')
    plt.title('Average temperature in each month')
    plt.show()


# If file is run call main
if __name__ == "__main__":
    main()
