import json
from csv import DictReader

books = []
dates = []

with open('books.csv', newline='') as f:
    d_reader = DictReader(f)
    for row in d_reader:
        books.append(row)

with open("users.json", "r") as f:
    users = json.loads(f.read())

for user, book in zip(users, books):
    data = {'name': user['name'], 'gender': user['gender'], 'address': user['address'],
            'book': [{'title:': book['Title'],
                      'author': book['Author'],
                      'height': book['Height']}]}
    dates.append(data)

with open("readers.json", "w") as f:
    s = json.dumps(dates, indent=4)
    f.write(s)
