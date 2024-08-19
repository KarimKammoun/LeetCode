a=11
def premier(a,mx):
    if mx==1:
        return True
    if a==1:
        return True
    res=(mx%a!=0)
    return res==premier((a-1),mx)==True
print(premier(a-1,a))