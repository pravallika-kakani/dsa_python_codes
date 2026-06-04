def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    lhalf = nums[:mid]
    rhalf = nums[mid:]
    lhalf = mergesort(lhalf)
    rhalf = mergesort(rhalf)
    return merge(lhalf, rhalf)
def merge(l, r):
    new = []
    i, j =0, 0
    while i<len(l) and j< len(r):
        if l[i]<r[j]:
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1
    new.extend(l[i:])
    new.extend(r[j:])
    return new
nums = [12, 1, 23, 45, 90, 11, 9]
nums = mergesort(nums)
print("sorted array:", nums)
#Output: sorted array: [1, 9, 11, 12, 23, 45, 90]
