x=input()
lc,uc,ev,od='','','',''
for i in range(len(x)):
    if(x[i].islower()):
        lc+=x[i]
    elif(x[i].isupper()):
        uc+=x[i]
    elif(int(x[i])%2==0):
        ev+=x[i]
    else:
        od+=x[i]
print (''.join(sorted(lc)+sorted(uc)+sorted(ev)+sorted(od)))