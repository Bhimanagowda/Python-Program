class Student:
  
  school="SSIT"
  #Instance method
  def __init__(self,m1,m2,m3): 
    self.m1=m2
    self.m2=m2
    self.m3=m3
    
  def avg(self):   #IntanceMethod
    return (self.m1+self.m2+self.m3)/3
  
  @classmethod   #classmethod
  def schoolinfo(cls):
    return cls.school
  
  @staticmethod  #ststicMethod
  def info():
    print("this is staticmethod")
  
s1=Student(90,80,70)
print(s1.avg())
print(s1.school)
print(s1.info())