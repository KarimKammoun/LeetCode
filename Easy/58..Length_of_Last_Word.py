class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=0
        res=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                j=i
                while s[j]!=" " and j>=0:
                    res=res+1
                    j=j-1
                return res