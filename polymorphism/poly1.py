class Car:
  def mil():
    pass
  
class BMW(Car):
  def mil(self):
    print("10KM/hr")
    
class Swift(Car):
  def mil(self):
    print("20KM/hr")

class Zen(Car):
  def mil(self):
    print("25KM/hr")

class Kia(Car):
  def mil(self):
    print("17KM/hr")
    

def fun(car):
  car.mil()
  
b=BMW()
s=Swift()
z=Zen()
k=Kia()

fun(b)
fun(s)
fun(z)
fun(k)