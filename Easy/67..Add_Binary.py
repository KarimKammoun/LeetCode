class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        somme = bin(int(a, 2) + int(b, 2))
        somme_sans_prefixe = somme[2:]
        return(somme_sans_prefixe) 
                