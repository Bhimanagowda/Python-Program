class A:
  def feature1(self):
    print("Feature 1")
  def feature2(self):
    print("Feature 2")
    
class B(A):    #A extended to B
  def feature3(self):
    print("Feature 3")
  def feature4(self):
    print("Feature 4")
    
a1=A()
a2=A()
b1=B()
b2=B()
print(a1.feature1())
print(a2.feature2())

print(b1.feature1())  #here B class extend A class features
print(b2.feature2())  #here B class extend A class features
print(b1.feature3())
print(b2.feature4())