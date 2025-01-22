from menu_terminal import * 

def start():
    print("Welcome to my version of the 'Klotski'!")
    print("Chose if you would like to start or quit")
    print("     Start (1)")
    print("     Quit (2)")
    choice = input("Please choose the number of your choice (ex: 1): ")

    while choice not in ['1', '2']:
        print("Wrong input, please try again")
        choice = input("Please choose the number of your choice (ex: 1): ")

    if choice == '1':
        start_terminal()
    else:
        exit()

start()