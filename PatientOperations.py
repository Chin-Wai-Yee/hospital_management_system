from Patient import Patient
from Search import findPatient
from SickRecordOperation import addRecord
from ScreenHandle import *
from Operations import Status

# def onError(func, input_msg : str, error_msg : str):
#     def wrapper(object):
#         user_input = input(input_msg)
#         if (user_input == "0"):
#             return Status.EXIT
#         if (func(user_input)) == False:
#             alert(error_msg)
#             return Status.LOOP
#         return Status.PROCEED
#     return wrapper

def InputPatientID(patients : list[Patient], allow_duplicate = False) -> Status:
    def wrapper(patient : Patient):
        p_id = input("Please enter the patient's ID (0 - exit) : ")
        i = findPatient(patients, p_id)
        if p_id == "0":
            return Status.EXIT
        elif not allow_duplicate and i != -1:
            alert("Patient ID already exists. Please try again.")
        elif allow_duplicate and i == -1:
            alert("Patient ID not found. Please try again.")
        elif (patient.setId(p_id) == False):
            alert("Invalid ID. Please try again.")
            return Status.LOOP

        return Status.PROCEED
    
    return wrapper

def InputPatientName(patient : Patient) -> Status:
    p_name = input("Please enter the patient's Name (0 - Exit): ")
    if p_name == "0":
        return Status.EXIT
    if (patient.setName(p_name) == False):
        # actually won't happen
        alert("Invalid Name. Please try again.")
        return Status.LOOP

    return Status.PROCEED

def InputPatientAddress(patient : Patient) -> Status:
    p_addr = input("Please enter the patient's Address (0 - Exit): ")
    if p_addr == "0":
        return Status.EXIT
    if (patient.setAddress(p_addr) == False):
        alert("Invalid Address. Please try again.")
        return Status.LOOP

    return Status.PROCEED

def InputPatientAllergics(patient : Patient) -> Status:
    p_allergics = input("Please enter the patient's Allergics (0 to stop) : ")
    if (p_allergics == "0"):
        return Status.PROCEED
    elif (patient.setAllergics(p_allergics) == False):
        alert("Allergics existed. Please try again.")
    return Status.LOOP

def InputPatientSickRecord(patient : Patient) -> Status:
    while addRecord(patient) != Status.PROCEED:
        pass
    return Status.LOOP

def addPatient(patients : list[Patient]) -> None:
    step = 1
    new_patient = Patient()
    functions = [
        InputPatientID(patients),
        InputPatientName,
        InputPatientAddress,
        InputPatientAllergics,
        InputPatientSickRecord
    ]

    # Loop through each step
    while step <= len(functions):
        cls()
        print(new_patient)
        if (status := functions[step - 1](new_patient)) == Status.EXIT:
            break
        if status == Status.PROCEED:
            step += 1

    # Add patient to list
    if step == len(functions) + 1:
        patients.append(new_patient)

def editPatient(patients : list[Patient]):
    step = 1
    i : int
    while step == 1:
        p_id = input("Please enter the patient's ID to edit (0 - exit): ")
        if p_id == "0":
            step = -1
        elif i := findPatient(patients, p_id) == -1:
            print("Patient ID not found. Please try again.")
        else:
            step += 1

    while step == 2:
        print("1. Edit ID")
        print("2. Edit Name")
        print("3. Edit Address")
        print("4. Edit Allergics")
        print("5. Edit History of sickness")
        print("6. Exit")
        option = input("Please enter what you want to edit : ")
        # written by copilot
        if option == "1":
            p_id = input("Please enter the patient's ID : ")
            if (patients[i].setId(p_id) == False):
                print("Invalid ID. Please try again.")
            else:
                step += 1
        elif option == "2":
            p_name = input("Please enter the patient's Name : ")
            if (patients[i].setName(p_name) == False):
                # actually won't happen
                print("Invalid Name. Please try again.")
            else:
                step += 1
        elif option == "3":
            p_addr = input("Please enter the patient's Address : ")
            if (patients[i].setAddress(p_addr) == False):
                print("Invalid Address. Please try again.")
            else:
                step += 1
        elif option == "4":
            option = input("Enter 1 to add allergics, 2 to remove allergics : ")
            if option == "1":
                p_allergics = input("Please enter the patient's Allergics (0 to stop) : ")
                if (p_allergics == "0"):
                    step += 1
                elif (patients[i].setAllergics(p_allergics) == False):
                    print("Allergics existed. Please try again.")
            elif option == "2":
                p_allergics = input("Please enter the patient's Allergics number to remove (0 to stop) : ")
                if (p_allergics == "0"):
                    step += 1
                elif (patients[i].removeAllergics(p_allergics) == False):
                    print("Allergics not found. Please try again.")
            else:
                print("Invalid option. Please try again.")
        elif option == "5":
            option = input("Enter 1 to add history of sickness, 2 to remove history of sickness : ")
            if option == "1":
                p_sick_record = input("Please enter the patient's History of sickness (0 to stop) : ")
                if (p_sick_record == "0"):
                    step += 1
                elif (patients[i].setSickRecord(p_sick_record) == False):
                    # actually won't happen
                    print("Invalid History of sickness. Please try again.")
            elif option == "2":
                p_sick_record = input("Please enter the patient's History number to remove (0 to stop) :")
                if (p_sick_record == "0"):
                    step += 1
                elif (patients[i].removeSickRecord(p_sick_record) == False):
                    print("History not found. Please try again.")
            elif option == "6":
                step += 1
        else:
            print("Invalid option. Please try again.")

def deletePatient(patients : list[Patient]):
    step = 1
    i : int
    while step == 1:
        p_id = input("Please enter the patient's ID to delete (0 - exit): ")
        if p_id == "0":
            step = -1
        elif i := findPatient(patients, p_id) == -1:
            print("Patient ID not found. Please try again.")
        else:
            step += 1
    while step == 2:
        option = input("Are you sure you want to delete this patient? (Y/N) : ")
        if option == "Y":
            patients.pop(i)
            step += 1
        elif option == "N":
            step += 1
        else:
            print("Invalid option. Please try again.")

# Test
if __name__ == "__main__":
    patients : list[Patient] = []
    while True:
        print("1. Create new patient account")
        print("2. Edit patient account")
        print("3. Delete patient account")
        print("4. Add appointment date and treatment detail. List of medicine have been prescribed")
        print("5. Edit apppointment datae and treatment detail")
        print("6. Print bill for patient")
        print("7. Generate Report for each months")
        print("8. Exit system")
        option = input("Please enter your choice: ")
        if option == "1":
            addPatient(patients)
        elif option == "2":
            editPatient(patients)
        elif option == "3":
            deletePatient(patients)
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "6":
            pass
        elif option == "7":
            pass
        elif option == "8":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again")
        pause()
        cls()