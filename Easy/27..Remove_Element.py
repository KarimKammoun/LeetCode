class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        k=0
        while i <len(nums)-k:
            if nums[i]==val:
                nums.append(nums[i])
                nums.pop(i)
                k=k+1

            else:
                i=i+1
        return(len(nums)-k)