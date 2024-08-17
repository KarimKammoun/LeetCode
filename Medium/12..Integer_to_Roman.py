class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ch = str(num)
        res = ""
        for i in range(len(ch) - 1, -1, -1):
            if i == len(ch) - 1:  
                if "0" < ch[i] <= "3":
                    res = "I" * int(ch[i]) + res
                elif ch[i] == "4":
                    res = "IV" + res
                elif ch[i] == "5":
                    res = "V" + res
                elif "6" <= ch[i] <= "8":
                    res = "V" + "I" * (int(ch[i]) - 5) + res
                elif ch[i] == "9":
                    res = "IX" + res
            if i == len(ch) - 2:  
                if "0" < ch[i] <= "3":
                    res = "X" * int(ch[i]) + res
                elif ch[i] == "4":
                    res = "XL" + res
                elif ch[i] == "5":
                    res = "L" + res
                elif "6" <= ch[i] <= "8":
                    res = "L" + "X" * (int(ch[i]) - 5) + res
                elif ch[i] == "9":
                    res = "XC" + res

            if i == len(ch) - 3:  
                if "0" < ch[i] <= "3":
                    res = "C" * int(ch[i]) + res
                elif ch[i] == "4":
                    res = "CD" + res
                elif ch[i] == "5":
                    res = "D" + res
                elif "6" <= ch[i] <= "8":
                    res = "D" + "C" * (int(ch[i]) - 5) + res
                elif ch[i] == "9":
                    res = "CM" + res
            if i == len(ch) - 4:  
                if "0" < ch[i] <= "3":
                    res = "M" * int(ch[i]) + res
        return(res)
    


