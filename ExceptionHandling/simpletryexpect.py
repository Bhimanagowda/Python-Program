try:
  a=int(input("Enter the firstnumber"))
  b=int(input("Enter the Secondnumber"))
  c=a/b
  print(c) 
  # print("amith") 
  # raise TypeError
except:
  print("zero is not divided the number ")
finally:
  print("Finally block will be excuted")