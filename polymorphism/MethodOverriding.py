class A:
  def __init__(self):
    print("parents class")
    
class B(A):
  def __init__(self):
    super().__init__()
    print("child class")
    
b1=B()
print("************************************")
class A:
  def  show(self):
    print("parents class")
    
class B(A):
  def show(self):
    print("child class")
    
b1=B()
print(b1.show())


