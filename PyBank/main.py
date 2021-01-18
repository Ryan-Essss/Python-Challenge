# Import os module
import os

# module for reading csv files
import csv

# Grab csv
csvpath = os.path.join ('Resources', 'budget_data.csv')
# print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    # print(type(csvreader))

    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Set CSV variables
    total_months = 0
    net_total = 0
    
    # Setup months variables for Profit/Losses
    month_a = 0
    month_b = month_a + 1
    monthly_diff = 0
    avg_mdiff = 0
    great_inc = 0
    great_dec = 0
    month_inc = ""
    month_dec = ""
        
    # Variable Lists
    month_names = []
    monthly_values = []
    list_mdiff = []
    
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        net_total = int(row[1]) + net_total
        month_names.append(row[0])
        monthly_values.append(int(row[1]))

        # print(row)

    # Calculate the Profit/Loss per month   
    for month in monthly_values[1:]:
        monthly_diff = monthly_values[month_b] - monthly_values[month_a]
                
        if monthly_diff > great_inc:
            great_inc = monthly_diff
            month_inc = month_names[month_b]

        if monthly_diff < great_dec:
            great_dec = monthly_diff
            month_dec = month_names[month_b]

       
        list_mdiff.append(monthly_diff)

        month_a += 1
        month_b += 1

        # Prints Monthly Difference
        # print(f"Monthly Difference is {monthly_diff}")
        
# test list_mdiff
# print(list_mdiff)
# print(monthly_values)
# print (great_inc, month_inc)
# print (great_dec, month_dec)

avg_mdiff = round(sum(list_mdiff) / (total_months -1),2)
# print round(sum(list_mdiff))

# prints in terminal
print("Financial Analysis\n")
print("----------------------------------------\n")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_mdiff}")
print(f"Greatest Increase: {month_inc} (${great_inc})")
print(f"Greatest Decrease: {month_dec} (${great_dec})")

# creates a .txt file
f = open("Analysis\\analysis.txt", 'w')
f.write("Financial Analysis\n")
f.write("----------------------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${net_total}\n")
f.write(f"Average Change: ${avg_mdiff}\n")
f.write(f"Greatest Increase: {month_inc} (${great_inc})\n")
f.write(f"Greatest Decrease: {month_dec} (${great_dec})")
f.close()








  

     