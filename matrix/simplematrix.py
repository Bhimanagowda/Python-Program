a=[['Amith',98,67,87,65,88,75],
   ['Deepak',97,87,88,97,67,47],
   ["lavanya",97,89,77,89,77,76]
  ]
print(a)

n = 3
m = 4
serial_number = 1


# Replace values in a with serial numbers
for i in range(n):
    a[i] = [serial_number + j for j in range(m)]
    serial_number += m
print(a)

print(a[2][2])
a[1][0]=13
print(a)
