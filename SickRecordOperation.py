from Patient import SickRecord
from ScreenHandle import cls, alert, pause
from Operations import Status

def inputRecordName(record : SickRecord) -> Status:
    user_input =  input("Please input the record name (0 - Exit) : ")
    if user_input == "0":
        return Status.EXIT
    if record.setName(user_input) == False:
        alert("Invalid record name. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def inputRecordDate(record : SickRecord) -> Status:
    print ("Date Format: <YYYY-MM-DD>")
    print ("Example: 2021-12-31")
    user_input =  input("Please input the record date (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setDate(user_input) == False:
        alert("Invalid date. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def inputRecordTreatment(record : SickRecord) -> Status:
    user_input =  input("Please input the record treatment (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setTreatment(user_input) == False:
        alert("Invalid treatment. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def inputRecordDoctor(record : SickRecord) -> Status:
    user_input =  input("Please input the name of doctor (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setDoctor(user_input) == False:
        alert("Invalid doctor. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def printRecords(sick_records : list[SickRecord]) -> None:
    print("Sick Records")
    print("-------------------")
    for i, record in enumerate(sick_records):
        print(f"{i+1}. {record}")

def addRecord(sick_records : list[SickRecord]) -> Status:

    step = 1
    new_record = SickRecord()
    functions = [
        inputRecordName,
        inputRecordDate,
        inputRecordTreatment,
        inputRecordDoctor
    ]

    # Loop through each step
    while step <= len(functions):
        cls()
        print(sick_records)
        print("=" * 20)
        print(f"New record : {new_record}")
        if (status := functions[step - 1](new_record)) == Status.EXIT:
            break
        elif status == Status.PROCEED:
            step += 1

    # Add record to patient
    if step == len(functions) + 1:
        sick_records.append(new_record)
        return Status.LOOP
    
    return Status.PROCEED

def editRecord(sick_records : list[SickRecord]) -> None:
    p_id = input("Please enter the no. of sick record (0 - Exit): ").upper()
    if p_id == "0":
        return
    try:
        p_id = int(p_id) - 1
    except ValueError:
        alert("Invalid number. Please try again.")
        return
    else:
        if p_id < 0 or p_id >= len(sick_records):
            alert("Invalid number. Please try again.")
            return
    record = sick_records[p_id]

    while True:
        cls()
        print(record)
        print("=" * 20)
        print("1. Edit Name")
        print("2. Edit Date")
        print("3. Edit Treatment")
        print("4. Edit Doctor")
        print("5. Exit")
        option = input("Please enter what you want to edit : ")
        # written by copilot
        if option == "1":
            inputRecordName(record)
        elif option == "2":
            inputRecordDate(record)
        elif option == "3":
            inputRecordTreatment(record)
        elif option == "4":
            inputRecordDoctor(record)
        elif option == "5":
            return
        else:
            alert("Invalid option. Please try again.")
    
def sickMenu(sick_records : list[SickRecord]) -> Status :
    operations = [
        "Add new sick record",
        "Edit sick record",
        "Delete sick record",
        "Exit"
    ]

    cls()
    printRecords(sick_records)
    print("=" * 20)

    for i, operation in enumerate(operations):
        print(f"{i+1:>2}. {operation}")
    
    option = input("Please enter your choice: ")
    if option == "1":
        addRecord(sick_records)
    elif option == "2":
        editRecord(sick_records)
        pass
    elif option == "3":
        # deleteRecord(sick_records)
        pass
    elif option == "4":
        return Status.EXIT
    else:
        alert("Invalid option, please try again")

    return Status.LOOP

# Test
if __name__ == "__main__":
    sick1 = SickRecord()
    sick1.setName("Covid-19")
    sick1.setDate("2020-05-05")
    sick1.setTreatment("Quarantine")
    sick1.setDoctor("Dr. John Doe")
    sick2 = SickRecord()
    sick2.setName("Flu")
    sick2.setDate("2019-05-05")
    sick2.setTreatment("Rest")
    sick2.setDoctor("Dr. Jane Doe")

    sick_records = [
        sick1,
        sick2
    ]
    while(sickMenu(sick_records) == Status.LOOP):
        cls()
        printRecords(sick_records)
        pause()