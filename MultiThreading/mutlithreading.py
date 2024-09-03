from time import sleep
from threading import *
class A(Thread):
  def run(self):
    for i in range(5):
      sleep(1)
      print("hi")

class B(Thread):
  def run(self):
    for i in range(5):
      sleep(1)
      print("hello")
      
t1=A()
t2=B()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()
print("bye")