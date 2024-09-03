def make_decorator(fun):
  
  def innerFun():
    print("amith")
    fun()
  return innerFun

@make_decorator
def simple_fun():
  print("it's deepak")
  
decor=make_decorator(simple_fun)
decor()