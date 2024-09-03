marks=int(input("Enter the Marks"))
if marks>100:
  print("Please,enter the valid marks between 0 to 100")
elif marks>=80 and marks<=100:
  print("firstClass")
elif marks>=60 and marks<=80:
  print("SecondClass")
elif marks>=50 and marks<=60:
  print("ThirdClass")
elif marks>=35 and marks<=50:
  print("pass")
else:
  print("fail")