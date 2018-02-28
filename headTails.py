# head or tails
from random import choice
print("\n  1. Head\n  2. Tails\n Press any other to exit")
print("\n Enter Your Choice : ",end="")
ch=input()

l=["Head","Tail"]
result=choice(l)
if ch=='1' and result=="Head" :
    print("\nIts ",result,", You Win :)")
elif ch=='2' and result=="Tail":
    print("\nIts ",result,", You Win :)")
elif ch=='1' or ch=='2':
    print("\nIts ",result,", You Lose :(")
else:
    print("\n Thank You for playing :)")
