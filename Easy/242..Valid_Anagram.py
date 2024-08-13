class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t))    :
            return False
        tab = [0]*26
        for i in range(len(s)) :
            tab[ord(s[i])-97]+=1
            tab[ord(t[i])-97]-=1
        for c in tab :
            if c != 0 :
                return False
        return True 