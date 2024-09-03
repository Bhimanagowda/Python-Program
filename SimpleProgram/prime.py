num=int(input("Enter the number"))
if num>1:
  print("type abouve 1 number")
count=0
for i in range(1,num+1):
  if num%i==0:
    count=count+1
if count == 2:
  print("its a prime number")
else:
  print("it's not prime number")

