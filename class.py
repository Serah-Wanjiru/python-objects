import datetime
class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def show_full_name(self):
        return f"Hello my name is {self.first_name}  {self.last_name}" 
    def year_of_birth(self):
      today=datetime.date.today().year
      
      return today - self.age
    def show_initials(self):
      return f"{self.first_name[0]} {self.last_name[0]} "     
x=Student(first_name="Serah",last_name="Wanjiru",age=18,country="Kenyan") 

 
         

   
        
