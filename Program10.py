l=[1,2,3,4,5,6,7,8,9]
newlst=[]
def func(lst):
    newlst.extend(lst[2::3])
    del(lst[2::3])
    return lst
while (len(l)>4):
    l=func(l)

print (newlst,l)