# num=[1,2,3,4,5]
for i in range(2,22,2):
  print(i) 
  
num=1
for i in range(5):
  print(i)

for i in range(4):
  for j in range(i+1):
    print("*",end=" ")
  print()
  
for i in range(4):
  for j in range(4-i):
    print("*",end=" ")
  print()