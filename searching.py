arr = eval(input("Enter the sorted array elements (e.g., [10, 20, 30]): "))
target = int(input("Enter the target: "))

# --- 1. Linear Search ---
print("\n--- Linear Search Result ---")
linear_found = False
for i in range(0, len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        linear_found = True
        break  

if not linear_found:
    print("Element not found")


# --- 2. Binary Search ---
print("\n--- Binary Search Result ---")
low = 0
high = len(arr) - 1
binary_found = False

while low <= high:
    mid = (low + high) // 2  
    
    if arr[mid] == target:
        print("Element found at index", mid)
        binary_found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1 

if not binary_found:
    print("Element not found")
