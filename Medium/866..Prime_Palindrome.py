class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        ch=str(n)
        def premier(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11
        if n<=2:
            return 2
        if n==5:
            return 5
        if n==7:
            return 7

        if (len(ch)%2)==0:
            l=10**((len(ch)//2)-1)
        else:
            l=10**(len(ch)//2)
        while True:
            ch=str(l)
            if premier(int(ch + ch[:-1][::-1]))== True and (int(ch + ch[:-1][::-1]))>=n :
                return int(ch + ch[:-1][::-1])
            if premier(int(ch + ch[::-1]))==True and (int(ch + ch[:-1][::-1]))>=n:
                return int(ch + ch[::-1])
            l=l+1