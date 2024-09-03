# a=int(input("Enter the a values"))
# b=int(input("Enter the b values"))
# c=int(input("Enter the c values"))
# def add(a,*k):
#   x=a
#   for i in k:
#    x=x+i
#   return x
# res=add(a,b,c)
# print(res)
# print("******************")

a=input("Enter the name ")
b=int(input("Enter the age"))
c=input("Enter the city values")
d=int(input("Enter the mobile number"))


def res(name,**k):
  print(f"name {name}")
  for i,j in k.items():
    print(i,j)
  
res(a,age=b,city=c,phone=d)

