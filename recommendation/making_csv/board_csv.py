import csv
import random
import string

# Define the table columns
columns = ['id', 'createdAt', 'updatedAt', 'title', 'content', 'writerId', 'totalViews', 'totalLikes']
title = []
writerId = []

for i in range(50):
	Id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	title.append(''.join(random.choices(string.ascii_letters + string.digits, k=8)))
	writerId.append(Id)

# Generate random data for each column
data = []
for _ in range(5000):
	row = [
		str(_),  # id
		'2022-01-01',  # createdAt
		'2022-01-01',  # updatedAt
		''.join(random.choice(title)),  # title
		'Content',  # content
		''.join(random.choice(writerId)),  # writerId
		random.randint(0, 500),  # totalViews
		random.randint(0, 250),  # totalLikes
	]
	data.append(row)

# Write the data to a CSV file
filename = '/Users/js0807/Desktop/dev/test/data/board.csv'
with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(columns)  # Write the column names
	writer.writerows(data)  # Write the data rows

print(f"CSV file '{filename}' created successfully.")
