#guessing game
from random import randint

secret_no=randint(1,100)
guess_count=5
flag=0

print("\n********** Guess Game **********\n")
while guess_count>0:
    print("You have ",guess_count," guesses left")
    no=eval(input("Enter your guess (1-100) : "))
    if no<1 or no>100:
        print("Number should be in range 1-100")
        exit()
    elif secret_no<no:
        print("Number is less than ",no,"\n")
    elif secret_no>no:
        print("Number is greater than ",no,"\n")
    elif secret_no==no:
        flag=1
        print("----  You Got It  ----")
        break
    guess_count-=1
print("\n Secret Number was ",secret_no,"\n")
if flag==0:
        print("---- You didnt got it , Dont worry Try Again ----")
