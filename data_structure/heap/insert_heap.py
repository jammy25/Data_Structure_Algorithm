# implementation of Heap

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

# largest so far compared with left child
    if left < n and arr[largest] < arr[left]:
        largest = left
# largest so far compared with left child
    if right < n and arr[largest] < arr[right]:
        largest = right
# change parent (swap values)
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)                           # recursive call


arr = [2, 66, 30, 5, 9, 10]
n = len(arr)

for i in range(n // 2 - 1, -1, -1):
    max_heapify(arr, n, i)

# Display
print("Max heap is:", )
for i in range(n):
    print(arr[i])