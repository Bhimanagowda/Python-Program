#square of number
# square=(x * x for x in range(1,11))
# for i in square:
#   print(i)

cars=['a','b','c','ws','f']
for i in range(0,len(cars)):
  print(cars[i])

print("*******************************")
#for using range
cars=['a','b','c','ws','f']
for i in range(len(cars)):
  print(cars[i])

bike={1:"a",2:"w",3:"f3"}
for key,info in bike.items():
  print(f"{key} : {info}")
  

#while
# n=77
# evencount=0
# oddcount=0

# i=1
# while i <= n:
#   if i%2==0:
#     evencount+=1
#   else:
#     oddcount+=1
#   i=i+1
# print(evencount,oddcount)