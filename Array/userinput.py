from array import *
arr=array('i',[]) #Empty array

n=int(input("Enter the length of a array"))
for i in range(n):
  x=int(input("enter the values to the array"))
  arr.append(x)
print(arr)

value=int(input("enter the values it shows in index array"))
index=arr.index(value)
print(f"the {value} of at psotion {index}")
