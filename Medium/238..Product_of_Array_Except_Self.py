class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        liste1=[1]*(len(nums)+1)
        liste2=[1]*(len(nums)+1)
        solution=[1]*len(nums)
        for i in range(2,len(nums)+2):
            liste1[-i]=liste1[-i+1]*nums[-i+1]
        for i in range(1,len(nums)+1):
            liste2[i]=liste2[i-1]*nums[i-1] 
        for i in range(len(nums)):
            solution[i]=liste1[i+1]*liste2[i]
        return solution