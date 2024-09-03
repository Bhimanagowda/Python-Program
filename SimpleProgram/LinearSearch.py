pos=-1

list=[66,48,45,35,28,25]
n=25

def search(lst,tar):
  global pos
  for i,value in enumerate(lst):
    if value==tar:
      pos=i
      return True
  return False

if search(list,n):
  print(f"it's found {pos+1}")
else:
  print("its not found")

