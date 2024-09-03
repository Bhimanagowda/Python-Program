
n=101
a=[]

for i in range(0,n):
    if i%2==0:
        a.append(i)


del a[1]
print(a) 

a.pop(0)
print(a)

a.remove(10)
print(a)

a.append(1000)
print(a)
a[-1]="amith"

print(a)
b=len(a)
print(b)

import array
x=array.array('i',[3,7,2,8,5])
x.append(10)
for i in x:
  print(i,end=" ")

j=i + [10,20,30]
print(j)