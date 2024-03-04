import os
from Patient import *

def menu() -> bool:

    operations = [
        "Create new patient account",
        "Edit patient account",
        "Delete patient account",
        "Add appointment date and treatment detail. List of medicine have been prescribed",
        "Edit apppointment datae and treatment detail",
        "Print bill for patient",
        "Generate Report for each months",
        "Exit system"
    ]

    for i, operation in enumerate(operations):
        print(f"{i+1:>2}. {operation}")

    option = input("Please enter your choice: ")

    match option:
        # Create patient
        case "1":
            pass
        # Edit patient
        case "2":
            pass
        # Delete patient
        case "3":
            pass
        # Add appointment
        case "4":
            pass
        # Edit appointment
        case "5":
            pass
        # Print bill
        case "6":
            pass
        # Generate report
        case "7":
            pass
        # Exit
        case "8":
            print("Exiting...")
            return False
        case _:
            print("Invalid option, please try again")
        
    return True

if __name__ == "__main__":
    patients : list[Patient] = []
    while(menu()):
        os.system("pause")
        os.system("cls")