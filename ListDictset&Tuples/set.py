set={"amith",33,(2,12,2023),"amith"}

#set[1]="amith" #set is immutable so can't change
set.add(3.33)
set.update([10,20,30])
print(set)

a={1,2,3,5,8,7,4}
b={3,5,7,9,2,1,6}
print(a.union(b))
print(a.intersection(b))

print(a.difference(b))
print(b.difference(a))

print(a.symmetric_difference(b))