# Name: Senhe Hao
# Assignment: Lab 9 part 3
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Main function
def main():
    # Reads in file
    input_file = open("WeatherDataWindows.csv", "r")
    days = input_file.readlines()
    del days[0]
    # Sets up variables
    i = 0
    maximum_temp = 0
    minimum_temp = 10000000
    precip_max = 0
    avg_temp_range = 0
    avg_dew_high_jan = 0
    days_where_avg_above_eighty = 0
    # Loops through the whole csv line by line
    for day in days:
        # Splits each day to calculate
        temp = day.split(",")
        # Checks max
        if int(temp[1]) > maximum_temp:
            maximum_temp = int(temp[1])
        # Checks min
        if int(temp[3]) < minimum_temp:
            minimum_temp = int(temp[3])
        # Checks if average temp is above 80
        if int(temp[2]) > 80:
            days_where_avg_above_eighty += 1
        # Adds precipitation of the day to the max
        precip_max += float(temp[13])
        i += 1
        # Adds the january high dew
        if temp[0][0] == "1":
            avg_dew_high_jan += int(temp[4])
        # Adds the range of temperature for the day.
        avg_temp_range += int(temp[1]) - int(temp[3])
    # Prints the results
    print("Highest temperature listed:", maximum_temp)
    print("Lowest temperature listed:", minimum_temp)
    print("Average daily precipitation is:", precip_max/i)
    print("Average temperature range is:", avg_temp_range/i)
    print("Average dew point high for Januaries is:", avg_dew_high_jan/i)
    print("There were", days_where_avg_above_eighty, "days where the average temperature was above eighty.")


# If file is run call main
if __name__ == "__main__":
    main()
