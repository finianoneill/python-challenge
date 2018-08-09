# module declarations
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# define count and storage variables
month_count = 0
total_profit = float(0)
greatest_increase = float(0)
increase_date = ""
greatest_decrease = float(0)
decrease_date = ""


# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first
	csv_header = next(csvreader)

	# loop through all of the rows in the data after the header
	for row in csvreader:

		# calculate the total number of months included in the dataset (each row is a month)
		month_count += 1

		# calculate the total net amount of "Profit/Losses" over the entire period
		total_profit += float(row[1])

		# calculate the greatest increase in profits (date and amount) over the entire period
		if float(row[1]) > 0:
			if float(row[1]) > greatest_increase:
				greatest_increase = float(row[1])
				increase_date = row[0]

		# calculate the greatest decrease in losses (date and amount) over the entire period
		if float(row[1]) < 0:
			if -float(row[1]) > greatest_decrease:
				greatest_decrease = float(row[1])
				decrease_date = row[0]

# calculate the average change in "Profit/Losses" between months over the entire period
average_change = total_profit / month_count

# create string to print to terminal based on the values calculated
print_string = ("Financial Analysis \n---------------------------- \nTotal Months: " + str(month_count) + 
	"\nTotal: $" + str(total_profit) + "\nAverage Change: $" + str(average_change) + "\nGreatest Increase in Profits: "
	+ str(increase_date) + " ($" + str(greatest_increase) + ") \nGreatest Decrease in Profits: " + str(decrease_date) +
	" ($" + str(greatest_decrease) + ")")

# in addition, print the analysis to the terminal and export a text file with the results.
print(print_string)

with open("Resources/Output.txt", "w") as text_file:
    print(print_string, file=text_file)