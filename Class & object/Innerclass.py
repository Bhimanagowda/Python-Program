class Student:
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno
    self.lab=self.Labtop()
    
  def show(self):
    return (self.name,self.rollno,self.lab.show())
    
  
  class Labtop:
    def __init__(self):
     self.brand="hp"
     self.version="8.3"
    
    def show(self):
       return (self.brand,self.version)
  
s1=Student('Amith',32)
print(s1.show())  

lab1=Student.Labtop()
print(lab1.show())