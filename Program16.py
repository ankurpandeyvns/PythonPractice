tstcs=int(input())
for x in range(tstcs):
    sz=[]
    leng=int(input())
    arr=input().split()
    for m in range(leng):
        print(arr[m:m+1])
    print (min(sz))