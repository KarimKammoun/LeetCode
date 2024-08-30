nums = [2,1,3,5,6]
k = 5
multiplier = 2


for i in range(k):
    min =0
    for j in range(len(nums)):
        if nums[j]<nums[min]:
            min =j
    nums[min]=nums[min]*multiplier
print(nums)
