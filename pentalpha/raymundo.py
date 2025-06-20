from os import system

def raymundo_profile():
    """Interactive menu to view Angella Jane Raymundo's profile details."""
    while True:
        system("cls")
        print("\nWelcome to Angella Jane Raymundo's Menu")
        print("------------------------------------------")
        print("[1] Hobbies")
        print("[2] Fun Fact")
        print("[3] Motto")
        print("[4] Managbanag - Comment")
        print("[5] Bautista - Comment")
        print("[6] Espinola - Comment")
        print("[7] Banzali - Comment")
        print("[0] Exit")
        print("------------------------------------------")

        choice = input("Enter your choice: ").strip().lower()

        match choice:
            case "1":
                system("cls")
                print("-------")
                print("Hobbies")
                print("-------")
                print("\nI enjoy designing user interfaces, learning " 
                        + "JavaScript frameworks, and playing video games.")
            case "2":
                system("cls")
                print("--------")
                print("Fun Fact")
                print("--------")
                print("\nI can play the guitar by listening, even without "
                        + "taking any lessons.")
            case "3":
                system("cls")
                print("------")
                print("Motto")
                print("------")
                print("\n“Design is not just what it looks like and "
                        + "feels like. Design is how it works.” – Steve Jobs")
            case "4":
                system("cls")
                print("Wow so many designs, Very good Angella Jane Raymundo!")
                print("Keep up the good work!")
            case "5":
                system("cls")
                print("------")
                print("Bautista - Comment")
                print("------")
                print("Nice hobby, didn't know learning Javascript is a hobby")
            case "6":
                system("cls")
                print("Your profile is inspiring! - Espinola")
            case "7":
                system("cls")
                print("You are talented and creative! Stay what you are.")
            case "0":
                print("\nExiting Raymundo's module...\n")
                break
            case _:
                print("\nInvalid option. Please try again.")

        input()