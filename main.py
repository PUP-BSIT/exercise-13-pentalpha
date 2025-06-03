from os import system
from pentalpha import bautista, managbanag

while (True):
    system('cls')
    print("Choose a member: ")
    print("[1] - Bautista")
    print("[2] - Banzali")
    print("[3] - Espinola")
    print("[4] - Managbanag")
    print("[5] - Raymundo")
    print("[0] - Exit")
    menu_choice = int(input("Enter Choice: "))

    match (menu_choice):
        case 1:
            bautista.bautista_profile()
        case 2:
            # TODO: (Banzali) Call banzali profile function
            pass
        case 3:
            # TODO: (Espinola) Call espinola profile function
            pass
        case 4:
            managbanag.managbanag_profile() 
            pass
        case 5:
            # TODO: (Raymundo) Call raymundo profile function
            pass
        case 0:
            break
