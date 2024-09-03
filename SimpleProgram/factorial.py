num=int(input("Enter the number"))
fact=1
for i in range(num,1,-1):
  fact=fact*i
print(fact)


#using method
def fact(num):
  fact=1
  for i in range(num,1,-1):
    fact=fact*i
  return fact
reslut=fact(num)
print(reslut)

#USing recursion
# def fact(num):
#   if num==0 or num==1: 
#     return 1
#   else:
#     return num*fact(num-1)
  
# res=fact(num)
# print(res)
