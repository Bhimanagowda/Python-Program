class A:
  def __init__(self,max=0):
    self.max=max
    
  def __iter__(self):
    self.n=0
    return self
  
  def __next__(self):
    if self.n<self.max:
      res= 2** self.n
      self.n+=1
      return res
    else:
      raise StopIteration
  
  
a=A(5)
iteration=iter(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))



