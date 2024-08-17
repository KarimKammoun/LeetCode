class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def verif (ch):
            if len(ch)<=1:
                return True
            if ch[0]==ch[-1]:
                test=True
            else:
                test=False
            return test==verif(ch[1:(len(ch)-1)])==True
        return(verif (str(x)))