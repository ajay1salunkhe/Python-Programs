

print("Enter An Integer : ")
no=int(input())
str=""
if no>0 and no<3:
    for i in range(1,no+1):
        str+="*"
        #print("*",end="")
else:
    for i in range(1,no+1):
        mid=no/2
        #print("mid : ",mid)
        if mid>i:
            str+="<"
            #print("<",end="")
        elif mid<i-1:
            str+=">"
            #print(">",end="")
        else:
            str+="*"
            #print("*",end="")

print(str)
