class A:
  def __init__(self):
    print("Class A")
  def Aabc(self):
    print("A:abc")
  def Axyz(self):
    print("A:xyz")     
  
class B(A):
  def __init__(self):
    super().__init__()
    print("Class B")
  def Babc(self):
    print("B:abc")
  def Bxyz(self):
    print("B:xyz")
    

b=B()
b.Aabc()
b.Axyz()
b.Babc()
b.Babc()