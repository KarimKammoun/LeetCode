class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct=0
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="I":
                if ct>=1:
                    res=res-1
                else:
                    ct=0
                    res=res+1
            if s[i]=="V":
                ct=1
                res=res+5
            if s[i]=="X":
                if ct>=3:
                    res=res-10
                else:
                    ct=2
                    res=res+10
            if s[i]=="L":
                ct=3
                res=res+50
            if s[i]=="C":
                if ct>=5:
                    res=res-100
                else:
                    ct=4
                    res=res+100
            if s[i]=="D":
                ct=5
                res=res+500
            if s[i]=="M":
                ct=6
                res=res+ 1000 
        return(res)