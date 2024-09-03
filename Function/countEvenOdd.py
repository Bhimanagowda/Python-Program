from array import *

arr=array("i",[])
num=int(input("Enter ther length of arrayy"))
for i in range(num):
  x=int(input("enter the values to the array"))
  arr.append(x)
  print(arr)
  
  def evenodd(arr):
    even=0
    odd=0
    for i in arr:
      if i%2==0:
        even+=1
      else:
        odd+=1
    return even,odd

even,odd=evenodd(arr)
print(even,odd)