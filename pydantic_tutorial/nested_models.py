from pydantic import BaseModel


class student(BaseModel):
    name:str
    age:int
    address:address
    

class address (BaseModel):
    city:str
    state:str
    code:int
    

address_1={"city":"lahore","state":"punjab","code":45}
address_1=address(**address_1)



student_1={"name":"hamza","age":22,"address":address_1}
student_1=student(**student_1)


def student_info(student:student):

 print(student)
 
 
student_info(student_1)