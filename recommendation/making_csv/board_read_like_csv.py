import csv
import random
import string

# Define the table columns
columns = ['id', 'liked', 'viewed', 'boardId', 'userId']

# Generate random data for each column
data = []
for _ in range(5000):
	row = [
		str(_),  # id
		random.choice([0, 1]),  # liked
		random.choice([0, 1]),  # viewed
		random.randint(0, 50),  # boardId
		random.randint(0, 50),  # userId
	]
	data.append(row)

# Write the data to a CSV file
filename = '/Users/js0807/Desktop/dev/test/data/board_read_like.csv'
with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(columns)  # Write the column names
	writer.writerows(data)  # Write the data rows

print(f"CSV file '{filename}' created successfully.")
