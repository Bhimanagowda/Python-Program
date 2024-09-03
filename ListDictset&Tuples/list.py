import math

print("math.perm(n, k): Returns the number of permutations of n items taken k at a time. ",math.perm(5, 2))  

print(" math.comb(n, k): Returns the number of combinations of n items taken k at a time",math.comb(5, 2))  #

print("square root:",math.sqrt(16)) 

print(math.pow(2,3))

print("factorial of 5:",math.factorial(5))

print(1,2,3,4,5,sep=",",end=".")
print()

c=[x for x in range(100) if x%2==0 and x%5==0]
print(c)

list1=["even" if x%2==0  else "odd" for x in range(20)]
print(list1)

list=[x for x in range(2,21) if x%2==0]
print(list)

a=[i for i in 'deepak']
print(a)

a=[]
for i in 'Amith':
  a.append(i)
print(a) 

#  

