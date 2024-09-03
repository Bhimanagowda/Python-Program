from functools import reduce
#function for filter
def even(n):
  return n%2==0

#function for map
def double(n):
  return n*2

#function for reduce
def sum(a,b):
  return a+b


nums=[4,7,2,8,0,4,5,6]

#evens=list(filter(even,nums))   #using filter function
evens=list(filter(lambda a:a%2==0,nums))
print(evens)

double=list(map(double,evens))   #using map function
#double=list(map(lambda a:a*2,evens))
print(double)

sum=reduce(sum,double)
#sum=reduce(lambda a,b:a+b,double)
print(sum)