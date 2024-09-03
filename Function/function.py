a=input("Enter the a values")
b=input("Enter the b values")

def name(fname,lname):
  print(f'{fname} & {lname}')

#name('amith',' **')

data=[a,b]
name(*data)

