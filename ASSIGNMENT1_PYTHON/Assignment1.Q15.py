import csv

# Specify the filename
filename = 'input_15.csv'

# Open the file and create a CSV reader
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Iterate through the rows in the CSV file and print each row
    for row in csvreader:
        print(row)
