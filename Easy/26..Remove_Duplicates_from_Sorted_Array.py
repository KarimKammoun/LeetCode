nums = [0,0,1,1,1,2,2,3,3,4]


k=0
i=1
while i<len(nums) :
    if nums[i]>nums[k] and nums[k]==nums[k+1]:
        nums[k+1]=nums[i]
        k=k+1
    i=i+1
    print(nums)




print(nums)
print(k) 