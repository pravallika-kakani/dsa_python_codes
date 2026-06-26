def right_rotate(nums):
    n=len(nums)
    temp=nums[n - 1]
    for i in range(n-1,-1,-1):
        nums[i]=nums[i - 1]
    nums[0]=temp
    return nums

nums=list(map(int, input().split()))
right_rotate(nums)
print(nums)

'''
INPUT: 1 2 3 4 5
OUTPUT: [5, 1, 2, 3, 4]
'''
