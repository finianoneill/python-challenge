# module declarations
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# create function that will check list for value
def check_list(checked_list, checked_value):
	final_truth = False
	for element in checked_list:
		if element[0] == checked_value:
			final_truth = True
			break

	return final_truth

# create function that will pull out index of found value
def find_index(checked_list, checked_value):
	for element in checked_list:
		if element[0] == checked_value:
			return checked_list.index(element)

def find_max(checked_list):
	max_value = 0.0
	max_winner = ""
	for element in checked_list:
		if float(element[1]) > max_value:
			max_value = float(element[1])
			max_winner = element[0]
	return max_winner

# define count and storage variables
vote_count = 0
candidate_list = []


# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	# Read the header row first
	csv_header = next(csvreader)

	# loop through all of the rows in the data after the header
	for row in csvreader:

		# count the total number of votes cast
		vote_count += 1

		# develop complete list of candidates who received votes
		if check_list(candidate_list, row[2]) == False:
			candidate_list.append([row[2], 0])
		else:
			# calculate the percentage of votes each candidate won and count of votes won
			candidate_list[find_index(candidate_list, row[2])][1] += 1

# create first string to output to file and terminal
first_print_string = ("Election Results \n------------------------- \nTotal Votes: " +
	str(vote_count) + "\n-------------------------\n")

# create second string to output to file and terminal
second_print_string = ""
for candidate in candidate_list:
	second_print_string += (candidate[0] + ": " + str(round((float(candidate[1]) / float(vote_count)) * 100, 2)) + "% (" +
		str(candidate[1]) + ") \n") 

# create third and final string to output to file and terminal
third_print_string = ("------------------------- \nWinner: " + find_max(candidate_list) + 
	"\n-------------------------")

final_string = first_print_string + second_print_string + third_print_string

# print final message to terminal and output file
print(final_string)

with open("Resources/Output.txt", "w") as text_file:
    print(final_string, file=text_file)
