import re
def sumdgt(Number):    
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum
x=input()
fnl=sum(map(int,re.findall(r'\d+',x)))
while(fnl>9):
    fnl=sumdgt(fnl)
print (fnl)