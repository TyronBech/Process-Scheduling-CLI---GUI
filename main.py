import os
from cli import cli_object
from gui import gui_object

def main():
    while True:
        os.system("cls")
        print("A - CLI Method")
        print("B - GUI Method")
        choice = input("Choose one option: ").upper()
        if choice == "A":
            cli_object()
            break
        elif choice == "B":
            gui_object()
            break
        else:
            print("Invalid input, please try again")
            os.system("pause")

if __name__ == "__main__":
    main()