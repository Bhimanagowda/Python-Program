# Python does not natively support method overloading in the traditional sense. In Python, a class can only have one method with a given name. When you define a method multiple times with the same name, the last definition overwrites the previous ones.
class Example:
    def add(self,*args):
      if len(args)==1:
        print(args[0])
      elif len(args)==2:
        print(args[0]+args[1])
      elif len(args)==3:
       print(args[0]+args[1]+args[2])
      else:
        print("invalid")

obj = Example()

obj.add(10, 20, 30)  
obj.add(10, 20)    
obj.add(10)

# def add(*args):
#   if len(args)==2:
#       print(args[0]+args[1])
#   elif len(args)==3:
#       print(args[0]+args[1]+args[2])
#   elif len(args)==4:
#      print(args[0]+args[1]+args[2]+args[3])
#   else:
#     print("invalid")
  
  
# add(1,2)
# add(1,2,3)
# add(1,2,4,5)


  
