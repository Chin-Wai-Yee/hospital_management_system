from Patient import SickRecord, Patient
from ScreenHandle import cls, alert
from Operations import Status

def addRecord(patient : Patient) -> Status:

    step = 1
    new_record = SickRecord()
    functions = [
        InputRecordName,
        InputRecordDate,
        InputRecordTreatment,
        InputRecordDoctor
    ]

    # Loop through each step
    while step <= len(functions):
        cls()
        print(patient)
        print("=" * 20)
        print(f"New record : {new_record}")
        if (status := functions[step - 1](new_record)) == Status.EXIT:
            break
        elif status == Status.PROCEED:
            step += 1

    # Add record to patient
    if step == len(functions) + 1:
        patient.setHistories(new_record)
        return Status.LOOP
    
    return Status.PROCEED

def InputRecordName(record : SickRecord) -> Status:
    user_input =  input("Please input the record name (0 - Exit) : ")
    if user_input == "0":
        return Status.EXIT
    if record.setName(user_input) == False:
        alert("Invalid record name. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def InputRecordDate(record : SickRecord) -> Status:
    print ("Date Format: <YYYY-MM-DD>")
    print ("Example: 2021-12-31")
    user_input =  input("Please input the record date (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setDate(user_input) == False:
        alert("Invalid date. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def InputRecordTreatment(record : SickRecord) -> Status:
    user_input =  input("Please input the record treatment (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setTreatment(user_input) == False:
        alert("Invalid treatment. Please try again.")
        return Status.LOOP
    return Status.PROCEED

def InputRecordDoctor(record : SickRecord) -> Status:
    user_input =  input("Please input the name of doctor (0 - Exit): ")
    if user_input == "0":
        return Status.EXIT
    if record.setDoctor(user_input) == False:
        alert("Invalid doctor. Please try again.")
        return Status.LOOP
    return Status.PROCEED

# Test
if __name__ == "__main__":
    p = Patient()
    addRecord(p)
    print("=" * 20)
    print(p)