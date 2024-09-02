class Solution(object):
    def findWords(self, words):
        liste=[0]*len(words)
        s1="qwertyuiop"
        s2="asdfghjkl"
        s3="zxcvbnm"
        res=[]
        for i in range(len(words)):
            for j in range(len(s1)):
                if s1[j] in words[i] or s1[j].upper() in words[i]:
                    liste[i]+=1
                    break
            for j in range(len(s2)):
                if s2[j] in words[i] or s2[j].upper() in words[i]:
                    liste[i]+=1
                    break
            for j in range(len(s3)):
                if s3[j] in words[i] or s3[j].upper() in words[i]:
                    liste[i]+=1
                    break
        for i in range(len(words)):
            if liste[i]==1:
                res.append(words[i])
        return(res)




