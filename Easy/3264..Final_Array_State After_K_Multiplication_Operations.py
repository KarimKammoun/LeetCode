class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            min =0
            for j in range(len(nums)):
                if nums[j]<nums[min]:
                    min =j
            nums[min]=nums[min]*multiplier
        return(nums)