from os import system

def managbanag_profile():
    """Function to display information about John Mark E. Managbanag"""
    while (True):
        system("cls")
        print("Whatsupp my name is John Mark E. Managbanag")
        print("1. Hobbies")
        print("2. Fun Fact")
        print("3. Motto")
        print("4. Bautista - Comment")
        print("5. Raymundo-comment")
        print("0. Exit")

        user_choice = int(input("Enter your choice: "))

        match (user_choice):
            case 1:
                print("I love playing basketball, watching anime,"
                        + " and going to gym")
            case 2:
                print("I once lost weight from 140kg to 95kg in just 6 months")
            case 3:
                print("'Keep pushing forward, no matter the obstacles!'")
            case 4:
                print("I miss your house hehe")
            case 5:
                print("You’ve got some really cool hobbies there.")
            case 0: 
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, please try again.")

        input("Press Enter to continue...")