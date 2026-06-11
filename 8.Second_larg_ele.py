nums =[55, 32, 97, -55, 45, 32, 88, 21, 97]
n = len(nums)
largest =float('-inf')
second_l= float('-inf')
for i in range(0,n):
    if(nums[i]>largest):
        second_l = largest
        largest = nums[i]
    elif(nums[i]> second_l and nums[i]!=largest):
        second_l = nums[i]
print(second_l)
'''
Output:
88
'''
