def left_rotate(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[n-1] = temp
    return nums
nums = list(map(int,input().split()))
left_rotate(nums)
print(nums)

'''
INPUT: 1 2 3 4 5
OUTPUT: [2, 3, 4, 5, 1]
'''
