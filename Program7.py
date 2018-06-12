import string
m,n=[],input().split()
str=string.ascii_lowercase[0:len(set(n))]
for x in range(len(str)):
    m.append([str[x],n[x]])
print (dict(m))