from pydantic import BaseModel
from typing import List,Dict,Optional


class Patient(BaseModel):
    name: str
    age: int
    weight:int
    married:Optional[bool] = None
    contact_info:Dict[str,str]
    allergies:List[str]


patient_info = {
    "name": "hamza",
    "age": 22,
    "weight": 72,
    
    "contact_info": {"number": "98765", "email": "kohat302@"},
    "allergies": ["pollen", "dust"],
}
patient_1 = Patient(**patient_info)


def insert_patient(patient: Patient):
    print(patient.age)
    print(patient.name)
    print(patient.contact_info)
    print(patient.married)
print(Patient)

insert_patient(patient_1)