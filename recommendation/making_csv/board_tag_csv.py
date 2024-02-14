import csv
import random
import string

# Define the table columns
columns = ['boardId', 'tagId']

# Generate random data for each column
data = []
for _ in range(50):
	row = [
		_,  # boardId
		random.randint(1, 5),  # tagId
	]
	data.append(row)

# Write the data to a CSV file
filename = '../data/board_tag.csv'
with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(columns)  # Write the column names
	writer.writerows(data)  # Write the data rows

print(f"CSV file '{filename}' created successfully.")
