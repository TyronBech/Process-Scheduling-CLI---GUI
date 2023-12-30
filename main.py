import os
from cli import cli_object
from gui import gui_object
def cli_method():
    cli_object()
def gui_method():
    gui_object()

def main():
    while True:
        os.system("cls")
        print("A - CLI Method")
        print("B - GUI Method")
        choice = input("Choose one option: ").upper()
        if choice == "A":
            cli_method()
            break
        elif choice == "B":
            gui_method()
            break
        else:
            print("Invalid input, please try again")
            os.system("pause")

if __name__ == "__main__":
    main()