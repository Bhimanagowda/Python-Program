from abc import ABC,abstractmethod

#Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function.
#An Abstract class can contain the both method normal and abstract method.
#An Abstract cannot be instantiated; we cannot create objects for the abstract class.

class Car(ABC):
  @abstractmethod
  def mileage(self):
    pass
  
class Telse(Car):
  def mileage(self):
    return "20km"
class Bmw(Car):
  def mileage(self):
    return "40km"
class Venu(Car):
  def mileage(self):
    return "90km"
t1=Telse()
print(t1.mileage())

b1=Bmw()
print(b1.mileage())

v1=Venu()
print(v1.mileage())

  