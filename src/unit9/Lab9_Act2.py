# Name: Senhe Hao
# Assignment: Lab 9 part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Main function
def main():
    # Reads in the input
    loan = float(input("Enter loan amount. "))
    original_loan = loan
    interest_rate = float(input("Enter the annual interest rate in percent. "))/100
    monthly = float(input("Enter monthly payment. "))
    name = input("Enter name for file. ") + ".csv"
    output_file = open(name, "w+", encoding="utf-8")
    # set up variables
    interest = 0
    i = 1
    output_list = ["Month,Amount of interest so far,Amount remaining on loan\n", "0,0,"+str(round(loan, 2))+"\n"]
    # While loop that continues until 30 if cannot pay off or until loan is paid off
    while True:
        # Loan calculations
        temp = round((interest_rate*loan)/12, 2)
        loan -= monthly
        interest += temp
        loan += temp
        # Makes sure the loan is never below 0
        if loan <= 0:
            loan = 0
        # Adds it onto the list that gets turned into a csv
        output_list.append(str(i) + "," + str(round(interest, 2)) + "," + str(round(loan, 2)) + "\n")
        # Conditions to check for. If loan is paid off or
        if loan <= 0:
            break
        if i == 30 and original_loan <= loan:
            break
        i += 1
    # Writes to file
    output_file.writelines(output_list)


# If file is run call main
if __name__ == "__main__":
    main()
