class Address:
    city : str = ""
    state : str = ""
    zip_code : str = ""

    def __init__(self, city, state, zip_code) -> None:
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Sick:
    name : str

class Patient:
    patient_id : str = ""
    patient_name : str = ""
    address : Address = None
    allergics : list[str] = []
    histories : list[Sick] = []

    def __init__(self, patient_id, patient_name, address, allergics, histories) -> None:
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.address = address
        self.allergics = allergics
        self.histories = histories

    def __str__(self) -> str:
        return (
              f"Patient ID  : {self.patient_id}\n\
                Patient Name: {self.patient_name}\
                Address     : {self.address}\
                Allergics   : {', '.join(self.allergics)}\
                Histories   : {', '.join(self.histories)}"
        )