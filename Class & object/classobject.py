class Car:
  wheel=5
  def __init__(self):
    self.name="BMW"
    self.mil="20"
    
c1=Car()
c1.wheel=6
c2=Car()
print(c1.name,c1.mil,c1.wheel)
print(c2.name,c2.mil)
