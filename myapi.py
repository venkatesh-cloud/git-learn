from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()
Student={
    1:{
        'name':'venkatesh',
        'age':23,
        'branch':'ECE'
    },
    2:{
        'name':'Sirish',
        'age':24,
        'branch':'EEE'
    }
}
class Students(BaseModel):
    name:str
    age:int
    branch:str
class UpdateStudents(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    branch:Optional[str]=None    

@app.get('/')
def first():
    return {"name":"venkatesh"}
@app.get('/Student')
def studentlist():
    return {'SudentList':Student}
@app.get('/Student/{stu_id}')
def getStudentbyid(stu_id:int=Path(None,description="Please enter student id u want",gt=0)):
    return {'Student':Student[stu_id]}
@app.get('/getby-Student_name')
def getdata( *,name:Optional[str]=None,test:int):#you should always use the default parameter first other wise use this way
    for i in Student:
        if Student[i]['name']== name:
            return Student[i]
    return {"data not found"}        
@app.post('/create-Student/{Stu_id}')
def createstudent(Stud_id:int,Stu:Students):
    if Stud_id in Student:
        return {'data':'Already exists'}
    Student[Stud_id]=Stu
    return Student[Stud_id]
@app.put('/update-student/{Stud_id}')
def update_student(Stud_id:int,stu:UpdateStudents):
    if Stud_id not in Student:
        return {"data":"Student does not exist"}  
    if stu.name!= None:
        Student[Stud_id]['name']=stu.name
    if stu.age!= None:
        Student[Stud_id]['age']=stu.age
    if stu.branch!=None:
        Student[Stud_id]['branch']=stu.branch
    return Student[Stud_id]   
@app.delete("/delete-student/{stud_id}")

def delete_student(stud_id:int):
    if stud_id not in Student:
        return {"Error":"Student does not exist"}
    del Student[stud_id]
    return {"Student data deleted succesfully"}    


      

            
                 