from fastapi import FastAPI,Path,Query
from fastapi import HTTPException
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    with open(os.path.join(BASE_DIR, "patients.json"), "r") as f:
        return json.load(f)
  

# router defifning hte url
@app.get("/")
def hello():
 return {"message":"patient management api"}




@app.get("/about")
def hello():
    return {"message":"complete sysytem to manage yourpatient data "}




@app.get("/view")
def view():
     data=load_data()
     return data
 
 
 
 
 
 
@app.get("/patient")
def all_patients():
    data =load_data()
    return data
 
@app.get('/patient/{patient_id}')
def view_patient(patient_id:  str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")





# // sorting data 


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
