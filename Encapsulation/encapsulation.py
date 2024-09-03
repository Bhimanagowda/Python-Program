class Persondetails:
  def __init__(self,name,age):
    self.name=name
    self._age=age
    self.__salary=30000
    
  def display(self):
    print(f"{self.name} and {self._age}")
    
  def set_salary(self,new_salary):
    if new_salary >=0:
      self.__salary=new_salary
    else:
      print("negative")
  
  def get_salary(self):
        print(f"updated salary  : {self.__salary}")

p=Persondetails("Amith",25)
p.display()

#access private attribute
print(f"initial salary : {p._Persondetails__salary}")

#access private method
p.set_salary(37383)
p.get_salary()

p1=Persondetails("Deepak",23)
p1.display()
print(f"initial salary : {p._Persondetails__salary}")
p1.set_salary(43534)
p1.get_salary( )