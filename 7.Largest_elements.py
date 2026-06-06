def larg_ele():
    n = len(nums)
    largest = nums[0]
    n =len(nums)
    for i in range(0, n):
        if(nums[i] > largest):
            largest = nums[i]
    return largest
nums = [55, 32, -97, 99, 3, 67]
print("Largest Element:", larg_ele())