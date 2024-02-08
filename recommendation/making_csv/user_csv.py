import csv
import random
import string
import uuid

# Define the table columns
columns = ['id', 'createdAt', 'updatedAt', 'uuid', 'nickname', 'farmId', 'username', 'password', 'name', 'age']

# Generate random data for each column
data = []
for _ in range(50):
	# Generate random UUID for 'uuid' column
	uuid_value = str(uuid.uuid4())
	row = [
		str(_),  # id
		'2024-02-01',  # createdAt
		'2024-02-01',  # updatedAt
		uuid_value,  # uuid
		''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # nickname
		str(_),  # farmId
		''.join(random.choices(string.ascii_letters + string.digits, k=5)),  # username
		''.join(random.choices(string.ascii_letters + string.digits, k=8)),  # password
		''.join(random.choices(string.ascii_letters, k=5)),  # name
		random.randint(18, 60)  # age
	]
	data.append(row)

# Write the data to a CSV file
filename = '../data/user.csv'
with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(columns)  # Write the column names
	writer.writerows(data)  # Write the data rows

print(f"CSV file '{filename}' created successfully.")
