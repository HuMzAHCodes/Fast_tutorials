from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int


patient_info = {"name": "hamza", "age": 22}

patient_1 = Patient(**patient_info)


def insert_patient(patient: Patient):
    print(patient.age)
    print(patient.name)


insert_patient(patient_1)