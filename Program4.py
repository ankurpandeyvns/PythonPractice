data=[]
for i in range(int(input("Enter how many details you want to fill:\n"))):
    name,marks=input("Enter the Name:\n"),int(input("Enter the marks:\n"))
    if(marks>=70 and marks<=80):
        grade="A"
    elif(marks>=81 and marks<=100):
        grade="A+"
    else:
        grade="B"
    data.append([name,grade])
print (data)
        