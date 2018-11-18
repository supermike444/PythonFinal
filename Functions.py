import csv


def searchbyname(searchterm):
    with open('food.csv', 'r') as foodfile:
        reader = csv.reader(foodfile)
        for row in reader:
            if searchterm in row[14].lower():
                print(row)
