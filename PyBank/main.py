# module declarations
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# define count variables
month_count = 0

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