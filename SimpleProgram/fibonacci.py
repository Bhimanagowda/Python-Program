

n=int(input("Ente the number"))
def fab(n):
  a,b=0,1
  print(a)
  print(b)
  for i in range(2,n):
      c=a+b
      a=b
      b=c
      print(c)
fab(n)

n=int(input("Ente the value"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
for i in range(1, num + 1):
    print(fibonacci(i), end=" ")

  