def reverse(arr, low, high):
    while(low<high):
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low+=1
        high-=1
    return arr
def l_rotate(arr, n, d):
    arr = reverse(arr, 0, d-1)
    arr = reverse(arr, d, n-1)
    arr = reverse(arr, 0, n-1)
    return arr

arr = list(map(int, input().split()))
print(l_rotate(arr, len(arr), 2))