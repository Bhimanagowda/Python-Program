class A:
  #class attributes
  name="Amith"
  #instantiate attributes
  def __init__(self,firstname,secondname):
    self.firstname=firstname
    self.secondname=secondname
  
  def display(self):
    print(f"{self.firstname} and {self.secondname}")
    
  def hen1(self):
    print("chicken")

class B(A):
  def __init__(self,firstname,secondname):
   super().__init__(firstname,secondname)

  def hen(self):
    print("chicken")
    
    
a=A("lavanya","sinchana")
b=B("amith","Deepak")

print(a.__class__.name)
a.display()
b.display()
