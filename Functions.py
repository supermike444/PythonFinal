import csv
import os
import datetime


def searchbyname(searchterm):
    with open('food.csv', 'r') as foodfile:
        reader = csv.reader(foodfile)
        print('Results:')
        for row in reader:
            if searchterm.lower() in row[14].lower():
                print(row[24] + ': ' + row[14])


def createprofile(name):
    if not os.path.isfile('profiles/' + name + '.csv'):
        with open('profiles/' + name + '.csv', 'w') as profile:
            writer = csv.writer(profile, lineterminator='\n')
            writer.writerow(['Date', 'Time', 'Food', 'Calories', 'Fat', 'Carbohydrates', 'Protein'])
    else:
        print('Profile already exists!')


def addfoodtoprofile(name, dbid):
    with open('food.csv', 'r') as foodfile:
        reader = csv.reader(foodfile)
        next(reader)
        for row in reader:
            if int(row[24]) == dbid:
                with open('profiles/' + name + '.csv', 'a') as profile:
                    writer = csv.writer(profile, lineterminator='\n')
                    now = datetime.datetime.now()
                    writer.writerow([now.strftime('%m/%d/%Y'), now.strftime('%H:%M:%S'), row[14], row[17], row[38], row[9], row[29]])

