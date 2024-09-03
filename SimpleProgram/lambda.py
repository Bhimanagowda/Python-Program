#map and filter
num=[3,5,7,33,66,23,45,67,35,63,34,64]
new_list=list(filter(lambda x: (x%2==0),num))
new_list1=list(map(lambda x:x*2,num))
print(new_list)
print(new_list1)

f=lambda a: a*a
res=f(10) 
print(res)

f=lambda a,b: a+b
res=f(10,20) 
print(res)

a=lambda x:x*2-10
print(a(100))

print(a)

print(type(a))