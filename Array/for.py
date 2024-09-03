import array

n=int(input("Enter the number"))
      
arr= array.array('i')
arr1= array.array('i')


# for i in range(1,100,2):
for i in range(n):
  if i%2==0:
    arr.append(i)
  else:
    arr1.append(i)
    
for x in arr:
  print(x,end=" " "")
  
print("\n")

for x in arr1:
  print(x,end=" ")


# for i in range(2,100,2):
#   print(i,end=" ")