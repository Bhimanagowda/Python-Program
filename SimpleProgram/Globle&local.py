x="100Global"
def fun():
  global y
  y="local"
  x="100" 
    
print(x)
fun()
print(x)
print(y)
  
