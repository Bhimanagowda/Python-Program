class Demo:
  def execute(self):
    print("hello")
    print("hi")
class Labtop:
  def code(self,ide):
    ide.execute()
    
ide=Demo()
lab=Labtop()
print(lab.code(ide))