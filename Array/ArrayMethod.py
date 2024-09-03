from numpy import *
from array import *
arr1=[7,2,8,5,1,6] 
arr2=[5,2,8,2,9,4]
a=array('i',[1,5,8,4,9])
print(a)
print("*******************************************")
#Sorterd 
print(sorted(arr1))
print(sorted(arr1, reverse=True))
print("*******************************************")
#concatenate
print(concatenate([arr1,arr2]))
print("*******************************************")
#copied

arr4=arr2.copy()
print(arr4)
print("*******************************************")
arr3=array(a.typecode,(b for b in a))
for i in arr3:
  print(i,end=" ")
  
# print(id(a))
# print(id(arr3))
