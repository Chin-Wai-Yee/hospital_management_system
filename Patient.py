from datetime import datetime
from Validations import idValidation, addrValidation

class Address:
    street : str = ""
    city : str = ""
    state : str = ""
    zip_code : str = ""
    country : str = ""

    # Constructor
    def __init__(
            self,
            street : str,
            city : str,
            state : str,
            zip_code : str,
            country : str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    # toString
    def __str__(self) -> str:
        if self.street == "" and self.city == "" and self.state == "" and self.zip_code == "" and self.country == "":
            return "None"
        return (
            f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"
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
            date : datetime = datetime.now(),
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

    def setDate(self, date: str) -> bool:
        try:
            self.date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False
        return True
    
    def setTreatment(self, treatment : str) -> bool:
        if treatment == "":
            return False
        self.treatment = treatment
        return True
    
    def setDoctor(self, doctor : str) -> bool:
        if doctor == "":
            return False
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
        return_str = (
            f"Patient ID   : {self.patient_id}\n"\
            f"Patient Name : {self.patient_name}\n"\
            f"Address      : {self.address}\n"\
            f"Allergics    : {', '.join(self.allergics) if self.allergics else 'None'}\n"\
        )

        if self.histories:
            return_str += "Histories    :\n"
            for i, record in enumerate(self.histories):
                return_str += f"{i+1}. {record}\n"
        else:
            return_str += "Histories    : None"

        return return_str
    
    def setId(self, id : str) -> bool:
        isId = idValidation(8, 4)
        if not isId(id):
            return False
        
        self.patient_id = id
        return True
    
    def setName(self, name : str) -> bool:
        if name == "":
            return False
        
        self.patient_name = name.title()
        return True
    
    def setAddress(self, address : str) -> bool:
        if not addrValidation(address):
            return False
        addr = [a.strip() for a in address.split(",")]
        self.address = Address(addr[0], addr[1], addr[2], addr[3], addr[4])
        return True
    
    def setAllergics(self, allergic : str) -> bool:
        if allergic == "":
            return False
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