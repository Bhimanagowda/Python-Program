name="amith"
city="tumkur"
marks=55.634
print("my name is %s and city %s." %(name,city))

print("my city is {1} and name is {0}." .format(name,city))

print("my name is {m} and lived in {n}.".format(m=name,n=city))

print("th marks is {0:f}%" .format(86.7456))

print("the marks is {0:.2f}%".format(78.43636))

print("the marks is {0:f}%".format(55))

print(f"my name is {name} and city{city},i got {marks}")

print(f"my name is{name.upper()},\n city{city.upper()}\n and marks(marks)")
statement=(f"name:{name},city:{city},marks:{marks}")
print(statement)

x=10
y=20 
print(f"x+y : {x+y}")
#print("the marks is {0:f}%".format('55')) #ValueError: Unknown format code 'f' for object of type 'str'


