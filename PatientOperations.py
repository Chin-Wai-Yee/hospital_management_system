from Patient import Patient
from Search import findPatient
from SickRecordOperation import sickMenu
from ScreenHandle import *
from Operations import Status

def inputPatient(patients : list[Patient]):
    def wrapper(patient : Patient):
        print("Patient ID Format: Four characters followed by four digits")
        print("Example: ABCD1234")
        p_id = input("Please enter the patient's ID (0 - exit) : ").upper()
        i = findPatient(patients, p_id)
        if p_id == "0":
            return Status.EXIT
        elif i != -1:
            alert("Patient ID already exists. Please try again.")
        elif (patient.setId(p_id) == False):
            alert("Invalid ID. Please try again.")
            return Status.LOOP

        return Status.PROCEED
    
    return wrapper

def inputPatientName(patient : Patient) -> Status:
    p_name = input("Please enter the patient's Name (0 - Exit): ")
    if p_name == "0":
        return Status.EXIT
    if (patient.setName(p_name) == False):
        alert("Invalid Name. Please try again.")
        return Status.LOOP

    return Status.PROCEED

def inputPatientAddress(patient : Patient) -> Status:
    print("Address Format: <Street>, <City>, <State>, <Zip>, <Country>")
    print("Example: 1234 Main St, Springfield, IL, 62701, USA")
    p_addr = input("Please enter the patient's Address (0 - Exit): ")
    if p_addr == "0":
        return Status.EXIT
    if (patient.setAddress(p_addr) == False):
        alert("Invalid Address. Please try again.")
        return Status.LOOP

    return Status.PROCEED

def inputPatientAllergics(patient : Patient) -> Status:
    p_allergics = input("Please enter the patient's Allergics (0 to stop) : ")
    if (p_allergics == "0"):
        return Status.PROCEED
    elif (patient.setAllergics(p_allergics) == False):
        alert("Allergics existed. Please try again.")
    return Status.LOOP

def inputPatientSickRecord(patient : Patient) -> Status:
    while sickMenu(patient.histories) != Status.EXIT:
        return Status.LOOP
    return Status.PROCEED

def addPatient(patients : list[Patient]) -> None:

    step = 1
    new_patient = Patient()
    functions = [
        inputPatient(patients),
        inputPatientName,
        inputPatientAddress,
        inputPatientAllergics,
        inputPatientSickRecord
    ]

    # Loop through each step
    while step <= len(functions):
        cls()
        print(new_patient)
        print("=" * 20)
        if (status := functions[step - 1](new_patient)) == Status.EXIT:
            break
        if status == Status.PROCEED:
            step += 1

    # Add patient to list
    if step == len(functions) + 1:
        patients.append(new_patient)

def editPatient(patients : list[Patient]):
    p_id = input("Please enter the patient's ID to edit (0 - exit): ").upper()
    if p_id == "0":
        return
    i = findPatient(patients, p_id)
    if i == -1:
        alert("Patient ID not found. Please try again.")
        return
        
    patient = patients[i]

    while True:
        cls()
        print(patient)
        print("=" * 20)
        print("1. Edit Name")
        print("2. Edit Address")
        print("3. Edit Allergics")
        print("4. Edit History of sickness")
        print("5. Exit")
        option = input("Please enter what you want to edit : ")
        # written by copilot
        if option == "1":
            inputPatientName(patient)
        elif option == "2":
            inputPatientAddress(patient)
        elif option == "3":
            inputPatientAllergics(patient)
        elif option == "4":
            while sickMenu(patient.histories) != Status.EXIT:
                pass
        elif option == "5":
            return
        else:
            alert("Invalid option. Please try again.")

def deletePatient(patients : list[Patient]):
    step = 1
    i : int
    while step == 1:
        p_id = input("Please enter the patient's ID to delete (0 - exit): ")
        if p_id == "0":
            step = -1
        elif i := findPatient(patients, p_id) == -1:
            alert("Patient ID not found. Please try again.")
        else:
            step += 1
    while step == 2:
        cls()
        print(patients[i])
        option = input("Are you sure you want to delete this patient? (Y/N) : ")
        if option == "Y":
            patients.pop(i)
            step += 1
        elif option == "N":
            step += 1
        else:
            alert("Invalid option. Please try again.")

# Test
if __name__ == "__main__":
    patients : list[Patient] = [
        Patient("ABCD1234", "John Doe"),
        Patient("EFGH5678", "Jane Doe")
    ]
    patients[0].setAddress("123 Main St, Los Angeles, CA, 90007, USA")
    patients[0].setAllergics("Peanuts")
    patients[0].setAllergics("UTAR")
    # Set diff data please
    patients[1].setAddress("456 Main St, Los Angeles, CA, 90007, USA")
    patients[1].setAllergics("Peanuts")
    patients[1].setAllergics("Human")

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
            alert("Invalid option, please try again")
        pause()
        cls()