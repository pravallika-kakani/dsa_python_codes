def sort(nums):
    n = len(nums)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

nums = [12, 1, 23, 45, 90, 11, 9]
sort(nums)
print("Sorted Array:", nums)