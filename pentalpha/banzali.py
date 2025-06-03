from os import system

def banzali_profile():
    """Display Grace Gabrielle Banzali's personal highlights."""
    while True:
        system("cls")
        print("==================================================")
        print("🌟 Welcome to Grace Gabrielle Banzali's Menu 🌟")
        print("==================================================")
        print("[1] Hobbies")
        print("[2] Fun Fact About Me")
        print("[3] Motto")
        print("[4] Managbanag - Comment")
        print("[5] Bautista - Comment")
        print("[0] Back to the Team Menu")
        print("==================================================")

        choice = input("Select an option (0–3): ")

        match choice:
            case '1':
                system("cls")
                print("============================================")
                print("+ + + + + + + + + HOBBIES + + + + + + + + + ")
                print("============================================")
                print("Playing Rubik's cube\nPlaying Guitar\nSelf-study\n"
                        + "Coding\nWalk therapy\nMaking art\nSolving puzzles")
                print("============================================")
            case '2':
                system("cls")
                print("============================================")
                print("+ + + + + + + + + FUN FACT + + + + + + + + +")
                print("============================================")
                print("* I can solve a Rubik's cube in under 15 \nseconds.\n" 
                        + "* I was born with closed ears, and my \n"
                        + "brother taped them so they'd open.")
                print("============================================")
            case '3':
                system("cls")
                print("============================================")
                print("+ + + + + + + + + + MOTTO + + + + + + + + + ")
                print("============================================")
                print("Knowing your own mind is the solution to \n"
                        +"all our problems.\n"
                        + "- Lama Yeshe")
                print("============================================")
            case '4':
                system("cls")
                print("Wow Tallented, i cant even solve a Rubik's cube!\n")
            case '5':
                system("cls")
                print("============================================")
                print("+ + + + + + + +  Bautista + + + + + + + + + ")
                print("============================================")
                print("You do too much sometimes. Just chill okay")
                print("============================================")
            case '0':
                print("\nHeading back to the Team Menu...")
                break
            case _:
                print("\nPlease pick a number between 0 and 3.")
            
        input()