from os import system

def bautista_profile():
    """ Prints information about John Matthew Bautista """
    while (True):
        system('cls')
        print("Hello! I'm John Matthew Bautista")
        print("[1] - Hobbies")
        print("[2] - Fun Fact")
        print("[3] - Motto")  
        print("[4] - Managbanag - Comment")
        print("[0] - Exit")

        menu_choice = int(input("Enter Choice: "))

        match (menu_choice):
            case 1:
                print("My hobbies are: Drawing and Coding")
            case 2:
                print("A fun fact about me is that I only weigh 36kgs")
            case 3:
                print("My motto in life is: 'Matulog ng maaga, "
                        + "upang buhay ay sumigla'")
            case 4:
                print("Wow! You are so good at drawing, John Matthew Bautista!")
                print("Keep up the good work!")
            case 0:
                break
            case _:
                print("Error: Wrong Input")

        input("Press enter to continue")
                
        