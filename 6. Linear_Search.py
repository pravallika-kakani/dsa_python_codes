def linear(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1
arr = [12, 1, 23, 45, 90, 11, 9]
target = 23
print(linear(arr, target))
target = 34
print(linear(arr, target))
'''
Output:
2
-1
'''
