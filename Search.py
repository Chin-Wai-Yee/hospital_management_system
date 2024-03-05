from Patient import Patient

# Search for patient by ID
def findPatient(patients : list[Patient], patientID):
    # return index of patient in list
    for i in range(len(patients)):
        if patients[i].id == patientID:
            return i
    return -1
