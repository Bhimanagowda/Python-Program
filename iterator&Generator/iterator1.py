n=int(input("Enter the number"))
list=[]

for i in range(n):
  x=int(input("enter the values to be inserted"))
  list.append(x)
print(list)     

a=iter(list)

print(next(a))
print(next(a))
print(next(a))
print(next(a)) # if we give one more iterationmit give error 

#or use this One
# print(a.__next__())
# print(a.__next__())