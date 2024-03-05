from datetime import datetime
from Validations import idValidation, addrValidation

class Address:
    no : str = ""
    street : str = ""
    city : str = ""
    state : str = ""
    zip_code : str = ""

    # Constructor
    def __init__(
            self, no : str,
            street : str,
            city : str,
            state : str,
            zip_code : str) -> None:
        self.no = no
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    # toString
    def __str__(self) -> str:
        if self.no == "":
            return ""
        return (
            f"{self.no} {self.street}, {self.city}, {self.state} {self.zip_code}"
        )

class SickRecord:
    name : str
    date : datetime
    treatment : str
    doctor : str

    # Constructor
    def __init__(
            self,
            name : str = "",
            date : datetime = None,
            treatment : str = "",
            doctor : str = "") -> None:
        self.name = name
        self.date = date
        self.treatment = treatment
        self.doctor = doctor

    # toString
    def __str__(self) -> str:
        return (
            f"{self.name} ({self.date.strftime('%Y-%m-%d') if self.date else ''})\n"\
            f"{self.treatment} by Dr. {self.doctor}"
        )
    
    def setName(self, name : str) -> bool:
        self.name = name
        return True

    def setDate(self, date : str) -> bool:
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False
        self.date = date
        return True
    
    def setTreatment(self, treatment : str) -> bool:
        self.treatment = treatment
        return True
    
    def setDoctor(self, doctor : str) -> bool:
        self.doctor = doctor
        return True

class Patient:
    patient_id : str
    patient_name : str
    address : Address
    allergics : list[str]
    histories : list[SickRecord]

    # Constructor
    def __init__(
            self,
            patient_id : str = "",
            patient_name : str = "",
            address : Address = Address("", "", "", "", ""),
            allergics : list[str] = [],
            histories : list[SickRecord] = []) -> None:
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.address = address
        self.allergics = allergics
        self.histories = histories

    # toString
    def __str__(self) -> str:
        return (
            f"Patient ID   : {self.patient_id}\n"\
            f"Patient Name : {self.patient_name}\n"\
            f"Address      : {self.address}\n"\
            f"Allergics    : {', '.join(self.allergics) if self.allergics else 'None'}\n"\
            f"Histories    : {', '.join(str(history) for history in self.histories) if self.histories else 'None'}"
        )
    
    def setId(self, id : str) -> bool:
        isId = idValidation(8, 4)
        if not isId(id):
            return False
        
        self.patient_id = id
        return True
    
    def setName(self, name : str) -> bool:
        self.patient_name = name.title()
        return True
    
    def setAddress(self, address : str) -> bool:
        if not addrValidation(address):
            return False
        address = [a.strip() for a in address.split(",")]
        self.address = Address(address[0], address[1], address[2], address[3], address[4])
        return True
    
    def setAllergics(self, allergic : str) -> bool:
        allergic = allergic.title()
        if allergic in self.allergics:
            return False
        self.allergics.append(allergic)
        return True
    
    def setHistories(self, history : SickRecord) -> bool:
        self.histories.append(history)
        return True
        
    def removeAllergics(self, n : int) -> bool:
        try:
            self.allergics.pop(n)
        # If n is out of range
        except IndexError:
            return False
        return True
    
    def removeHistories(self, n : int) -> bool:
        try:
            self.histories.pop(n)
        # If n is out of range
        except IndexError:
            return False
        return True

# Test 
if __name__ == "__main__":
    address = Address("123", "Main St", "Los Angeles", "CA", "90007")
    sick_record = [
        SickRecord("Covid-19", datetime(2020, 5, 5)),
        SickRecord("Flu", datetime(2019, 5, 5))
    ]
    patient = Patient("abcd1234", "John Doe", address, ["Peanuts", "UTAR"], sick_record)
    patient2 = Patient()
    print(patient)
    print('-'*50)
    print(patient2)
    # Output:
    # Patient ID  : abc123
    # Patient Name: John Doe
    # Address     : 123 Main St, Los Angeles, CA 90007
    # Allergics   : Peanuts
    # Histories   : Covid-19 (2020-05-05 00:00:00)