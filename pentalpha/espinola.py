from os import system

def espinola_profile():
    """ This is a menu that presents the user with a sample profile. """
    while True:
        system('cls')
        print("Hello! I'm Frankie Josh M. Espinola!\n")
        print("1. Hobbies")
        print("2. Goals")
        print("3. Motto")
        print("4. Managbanag - Comment")
        print("5. Bautista - Comment")
        print("6. Raymundo - Comment")
        print("7. Banzali - Comment")
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
            case 4:
                print("Wow! Motorist and gamerist at the same time")
                print("Keep up the good work!")
            case 5:
                print("Your training arc is just starting")
            case 6:
                print("That’s such a heartfelt and meaningful goal.")
            case 7: 
                print("You are adventurous bro! Just always ride safely.")
            case 0:
                break
            case _:
                print("Invalid number. Please enter another.")

        input()