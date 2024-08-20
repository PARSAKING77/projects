import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input, output):
    with open(input, 'r') as infile :
        reader = csv.reader(infile)
        data = list(reader)

        for row in data:
            print(f"{row[0]},{row[1]}")

    hash_dict = OrderedDict()

    for x in range(1000, 10000):
        password = str(x)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()


        hash_dict[hashed_password] = password

    result = []

    for user, hashed in data:
        if hashed in hash_dict:
            result.append(f"{user},{hash_dict[hashed]}")

    for res in result:
        print(res)


input = 'input.csv'
output = 'output.csv'

hash_password_hack(input, output)