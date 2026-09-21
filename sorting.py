
# 1. BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)
   
    for i in range(n):
       
        for j in range(0, n - i - 1):
           
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



# 2. QUICK SORT

def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[len(arr) // 2]
    
  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
  
    return quick_sort(left) + middle + quick_sort(right)



# 3. MERGE SORT

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
        

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            
 
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr



# 4. HEAP SORT

def heapify(arr, n, i):
    largest = i     
    left = 2 * i + 1 
    right = 2 * i + 2 

1
    if left < n and arr[left] > arr[largest]:
        largest = left

  
    if right < n and arr[right] > arr[largest]:
        largest = right

   
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)              
        
    return arr



test_data=eval(input("Enter array elements:"))

print("Original Array:", test_data)
print("Bubble Sort:   ", bubble_sort(test_data.copy()))
print("Quick Sort:    ", quick_sort(test_data.copy()))
print("Merge Sort:    ", merge_sort(test_data.copy()))
print("Heap Sort:     ", heap_sort(test_data.copy()))