class Solution(object):
    def groupAnagrams(self, liste1):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for i in liste1:
            liste = [c for c in i]
            liste.sort()
            s=''.join(liste)
            if s in dic:
                dic[s].append(i)
            else:
                dic[s]=[i]
        liste=[]
        for i in dic :
            liste.append(dic[i])
        return liste