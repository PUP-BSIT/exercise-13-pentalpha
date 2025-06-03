from os import system
from pentalpha import bautista, managbanag, raymundo, espinola, banzali

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
            banzali.banzali_profile()
        case 3:
            espinola.espinola_profile()
        case 4:
            managbanag.managbanag_profile() 
        case 5:
            raymundo.raymundo_profile()
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid input. Please choose from 0-5.")
        
    input()
