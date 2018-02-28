
print("Enter an integer : ")
no=int(input())
for i in range(0,no):
    for j in range(0,no):
        if i>0 and i<no-1:
            if j==0 or j==no-1:
                print("* ",end='')
            else:
                print("  ",end='')
        else:
            print("* ",end='')
    print()
