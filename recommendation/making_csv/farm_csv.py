import csv
import random
import string

# Define the table columns
columns = ['id', 'createdAt', 'updatedAt', 'name', 'userId', 'crop0', 'crop1', 'crop2', 'crop3']

# Generate random data for each column
data = []
for _ in range(50):
	row = [
		str(_),  # id
		'2024-02-08',  # createdAt
		'2024-02-08',  # updatedAt
		''.join(random.choices(string.ascii_lowercase, k=5)),  # name
		str(_),  # userId
		random.randint(0, 5),  # crop0
		random.randint(0, 5),  # crop1
		random.randint(0, 5),  # crop2
		random.randint(0, 5),  # crop3
	]
	data.append(row)

# Write the data to a CSV file
filename = '/Users/js0807/Desktop/dev/test/data/farm.csv'
with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(columns)  # Write the column names
	writer.writerows(data)  # Write the data rows

print(f"CSV file '{filename}' created successfully.")
