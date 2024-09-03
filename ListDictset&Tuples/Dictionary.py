dict={1:"Amith",3:"Deepak",4:"Shamanth"}

dict[2]="Lavanya" 
dict[5]="Megha"
dict.popitem()
print(dict)

print(dict.clear)

n=9
square={x:f"{n}*{x}= {n*x}" for x in range(1,11)}
for i in square:
 print(square[i])

n=5
for x in range(11):
  print(f"{n} * {x}={n*x}")
  