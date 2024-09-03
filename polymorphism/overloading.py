class Student:
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
    
  def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            return a + b + c
        elif a!=None and b!=None:
            return a + b
        else:
            return a
        
        

s1=Student(10,10)
print(s1.sum(10,20,30))
print(s1.sum(10,20))
print(s1.sum(10))
print()

# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2

#     def sum(self, a=None, b=None, c=None):
#         if a is not None and b is not None and c is not None:
#             return a + b + c
#         elif a is not None and b is not None:
#             return a + b
#         elif a is not None:
#             return a
#         else:
#             return 0

# s1 = Student(10, 10)
# print(s1.sum(10, 20, 30))  # Output: 60
# print(s1.sum(10, 20))      # Output: 30
# print(s1.sum(10))          # Output: 10
# print(s1.sum())            # Output: 0
