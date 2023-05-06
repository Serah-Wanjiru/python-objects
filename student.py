class Student:
    name="Serah"
    age=18
    school="AkiraChix"
    nationality="Kenyan"
    
student1=Student()    
print(student1.school)
student2=Student()

class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality): 
        self.name=name
        self.age=age
        self.nationality=nationality
    def greet_student(self):
        return f"Hello {self.name} welcome to {self.school}"
    def year_of_birth(self):
        year=2023-self.age
        return f"Hello {self.name} you were born in {year}"
      
   
        
elizabeth=Student(name="elizabeth",age=22,nationality="kenyan") 
jane=Student(name="jane",age=22,nationality="tanzanian") 
Sonia=Student(name="Sonia",age=22,nationality="Rwanda") 