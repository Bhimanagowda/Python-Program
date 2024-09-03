import array

# Create an array of signed integers
arr = array.array('i', [1, 2, 3, 4, 5])

count = arr.count(3)
print("Array:", count)
 
# Append an element
arr.append(6)
print("Array:", arr)


# Extend with more elements
arr.extend([7, 8])
print("Array:", arr)


# Insert an element
arr.insert(2, 10)
print("Array:", arr)

# Remove an element
arr.remove(10)
print("Array:", arr)


# Pop an element
last_element = arr.pop()
print("Array:", last_element)

# Find index of an element
idx = arr.index(5)
print("Array:", idx)

# Count occurrences of an element


# Reverse the array
arr.reverse()
print("Array:", arr)

# Convert to list
list_representation = arr.tolist()
print("Array:", list_representation)

# Print results
print("Array:", arr)


# print("Last element removed:", last_element)
# print("Index of 5:", idx)
# print("Count of 3:", count)
# print("List representation:", list_representation)
