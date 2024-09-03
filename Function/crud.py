def add(x,y):
  print("addition of two number")
  return(x+y)
def sub(x,y):
  print("addition of two number")
  return(x-y)
def mul(x,y): 
  print("addition of two number")
  return(x*y)
def div(x,y):
  print("addition of two number")
  return(x/y)

def menu():
  print("Main menu")
  print("1.For additional select that Number")
  print("2.For Subtraction select that Number")
  print("3.For multiplication select that Number")
  print("4.For division select that Number")
  choice=int(input("enter the number to be perform"))
  return choice

def calculation():
  choice=menu()
  num1=int(input("Enter the 1number"))
  num2=int(input("Enter the 2number"))
  if choice == 1:
    result=add(num1,num2)
  elif choice == 2:
    result=sub(num1,num2)
  elif choice == 2:
    result=mul(num1,num2)
  elif choice == 2:
    result=div(num1,num2)
  print("result=",result)
  
calculation()

  