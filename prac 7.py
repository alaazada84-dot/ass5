numbers = [5, 3, 4, 1, 2]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        print(x)
        j = i - 1
        # Move elements greater than x to one position ahead
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x

insertion_sort(numbers)
print(numbers)