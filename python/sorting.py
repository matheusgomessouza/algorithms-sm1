numbers = [6, 2, 9, 4, 7, 10, 12, 11, 14, 13]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

result = bubbleSort(numbers) 
print("BubbleSorted numbers:", result)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# result = insertionSort(numbers)
# print("Sorted numbers:", result)