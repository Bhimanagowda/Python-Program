class Animal:
  def sound(self):
    pass
class Cat(Animal):
  def sound(self):
    return "moo"
class Dog(Animal):
  def sound(self):
    return "bark"
class Cow(Animal):
  def sound(self):
    return "boo"
  
#common interface
def ani_sound(animal):
  print(animal.sound())
 
 
#object of class 
c1=Cat()
d1=Dog()
c2=Cow()

#pass the object to function
(ani_sound(c1))
(ani_sound(d1))
(ani_sound(c2))
