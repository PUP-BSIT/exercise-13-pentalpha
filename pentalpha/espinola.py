from os import system

def espinola_profile():
    """ This is a menu that presents the user with a sample profile. """
    while True:
        system('cls')
        print("Hello! I'm Frankie Josh M. Espinola!\n")
        print("1. Hobbies")
        print("2. Goals")
        print("3. Motto")
        print("0. Exit\n")

        menu_choice = int(input("Enter your choice: "))
    
        match (menu_choice):
            case 1: 
                print("My hobbies are: Riding Motorcyle, Playing Online Games")
            case 2:
                print("My goals is to graduate and help the family.")
            case 3:
                print("My motto in life is:")
                print("Hard is part of life. Pick yours.")
            case 0:
                break
        
        input()