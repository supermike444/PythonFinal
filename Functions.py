import csv
import os
import datetime


def getprofile(name):
    return 'profiles/' + name + '.csv'


def isvalidprofile(name):
    if os.path.isfile(getprofile(name)):
        return True
    print('Not a valid login')
    return False


def searchbyname():
    searchterm = input('Search term:\n')
    with open('food.csv', 'r') as foodfile:
        reader = csv.reader(foodfile)
        print('Results:')
        for row in reader:
            if searchterm.lower() in row[14].lower():
                print(row[24] + ': ' + row[14])


def createprofile(name):
    if not os.path.isfile(getprofile(name)):
        with open(getprofile(name), 'w') as profile:
            writer = csv.writer(profile, lineterminator='\n')
            writer.writerow(['Date', 'Time', 'Food', 'Calories', 'Fat', 'Carbohydrates', 'Protein'])
    else:
        print('Profile already exists!')


def deleteprofile(name):
    os.remove(getprofile(name))


def displayprofilehistory(name):
    with open('profiles/' + name + '.csv', 'r') as profile:
        reader = csv.reader(profile)
        for row in reader:
            print(row)


def addfoodtoprofile(name, dbid):
    with open('food.csv', 'r') as foodfile:
        exists = False
        reader = csv.reader(foodfile)
        next(reader)
        for row in reader:
            if int(row[24]) == int(dbid):
                exists = True
                with open('profiles/' + name + '.csv', 'a') as profile:
                    writer = csv.writer(profile, lineterminator='\n')
                    now = datetime.datetime.now()
                    writer.writerow([now.strftime('%m/%d/%Y'), now.strftime('%H:%M:%S'), row[14], row[17], row[38], row[9], row[29]])
        if not exists:
            print('Not a valid ID')


def addprompt(name):
    addfoodtoprofile(name, input('Food ID:\n'))


def doaction(name, action):
    if action == 'a':
        addprompt(name)
        return True
    elif action == 's':
        searchbyname()
        return True
    elif action == 'd':
        displayprofilehistory(name)
        return True
    elif action == 'l':
        return False
