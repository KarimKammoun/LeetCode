nums =10
ch=str(nums)
res=""
for i in range(len(ch)-1,-1,-1):
    if i==len(ch)-1:
        if "0"<ch[i]<="3":
            res="I"*(int(ch[i]))+res
        elif ch[i]=="4":
            res="IV"+res
        elif ch[i]=="5":
            res="V"+res
        elif "6"<=ch[i]<="8":
            res="V"+"I"*((int(ch[i]))-5)
        else:
            res="I"*(10-(int(ch[i])))+"X "+res
    if i==len(ch)-2:
        if "0"<ch[i]<="3":
            res="X"*(int(ch[i]))+res
        elif ch[i]=="4":
            res="XL"+res
        elif ch[i]=="5":
            res="L"+res
        elif "6"<=ch[i]<="8":
            res="L"+"X"*((int(ch[i]))-5)
        else:
            res="X"*(10-(int(ch[i])))+"c"+res
    """elif i==len(ch)-3:
        if "0"<ch[i]<="3":
            res="C"*(int(ch[i]))+res
        elif ch[i]=="4":
            res="CD"+res
        elif ch[i]=="5":
            res="D"+res
        elif "6"<=ch[i]<="8":
            res="D"+"C"*((int(ch[i]))-5)
        else:
            res="C"*(10-(int(ch[i])))+"M"+res
    else:
        res="M"*(10-(int(ch[i])))+res"""

    

print(res)

