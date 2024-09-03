class Voter(Exception):
  def __init__(self):
    super()
try:
  a=int(input("enter the age"))
  if a >18:
    print("eligiable to vote")
  else:
    raise TypeError
except TypeError:
  print("age is less then 18")
finally:
  print("end")

  