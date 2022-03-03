import csv
csv_columns = ['No','Name','Place']
dict_data = [
{'No': 1, 'Name': 'Prejin', 'Place': 'Kallara'},
{'No': 2, 'Name': 'Renjith', 'Place': 'Kallara'},
{'No': 3, 'Name': 'Aromal', 'Place': 'Muthuvila'},
{'No': 4, 'Name': 'Athmajan', 'Place': 'Pothencode'},
{'No': 5, 'Name': 'Akshay', 'Place': 'Kummil'},
]
csv_file = "names.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)

with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)