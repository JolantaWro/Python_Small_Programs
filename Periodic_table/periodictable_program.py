import csv

with open('periodictable.csv', mode='r', encoding='latin1') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)