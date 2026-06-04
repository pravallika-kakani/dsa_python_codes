def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= high and arr[i] <= p:
            i += 1
        while j >= low and arr[j] > p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j
nums = [12, 1, 23, 45, 90, 11, 9]
quick_sort(nums, 0, len(nums) - 1)

print("Sorted array:", nums)