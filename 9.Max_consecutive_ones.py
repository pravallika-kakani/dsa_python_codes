nums = list(map(int,input().split()))
count = 0
max_count = 0
for i in range(0, len(nums)):
    if(nums[i] == 1):
        count+=1
    else:
        if(count > max_count):
            max_count = count
        count = 0
if(count > max_count):
    max_count = count
print(max_count)