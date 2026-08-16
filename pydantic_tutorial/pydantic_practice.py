from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=30, title="name of person", description="give only max 30 chars long name", examples=["hamza", "haider"])]
    age: int
    email: EmailStr
    weight: Annotated[float,Field(gt=0,lt=130,strict=True)]
    linkedin: AnyUrl
    married: Annotated[Optional[bool], Field(default=None, description="either married or none")]
    contact_info: Dict[str, str]
    allergies: List[str]

patient_info = {
    "name": "hamza",
    "age": 22,
    "weight": 72,
    "email":"hu@gmail.com",
    "linkedin":"https://www.linkedin.com/",
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