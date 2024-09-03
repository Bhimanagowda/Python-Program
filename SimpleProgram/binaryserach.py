pos = -1

my_list = [33, 56, 32, 11, 66, 83]
n = 66

def search(lst, target):
    global pos
    l = 0
    u = len(lst) - 1
    
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == target:
            pos = mid  # Correctly update pos
            return True
        elif lst[mid] < target:
            l = mid + 1  # Move right
        else:
            u = mid - 1  # Move left
    return False

my_list.sort()

if search(my_list, n):
    print(f"Found at position {pos}")
else:
    print("Not found")
