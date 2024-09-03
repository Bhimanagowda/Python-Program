# 1.Using a List (Dynamic Array):
# Simply use an empty list, which is the most common type of dynamic array in Python.
# python
# arr = []


# 2.Using the array Module (Fixed-type Array):
# Use the array module if you need an array with a specific data type (e.g., integers or floats).
# python

# import array
# arr = array.array('i')  # Creates an empty array of integers

from array import *
import copy

n=int(input("enter the size for array"))
arr=array('i')

for i in range(n):
  x=int(input("enter the values to the array"))
  arr.append(x)
  
for x in arr:
   print(x,end=" ") 
print("\n *******************************************")

#reverse
arr.reverse()
print("ReverseOrder")
for i in arr:
  print(i ,end=" ")

print("\n *******************************************")

#copied
newarr=copy.copy(arr)
# newarr=array(arr.typecode, arr)

print("copied array",end=" ")
for i in newarr:
 print(f"{i}",end=" ")
print()



 