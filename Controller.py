import Functions


def main():
    while True:
        name = ''
        login = False
        while not login:
            yn = input('Returning user? y/n:\n')
            if yn == 'y':
                name = input('Login name:\n')
                login = Functions.isvalidprofile(name)
            elif yn == 'n':
                name = input('What should we call you?\n')
                Functions.createprofile(name)
                login = True
            else:
                print('That\'s not a y/n')

        while login:
            action = input('Action:\n')
            result = Functions.doaction(name, action)
            if not result:
                login = False


if __name__ == "__main__":
    main()
