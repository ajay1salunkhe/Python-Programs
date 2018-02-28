

#timer project
import time
counter=eval(input("\nSet Timer : "))

while counter>0:
    print(counter)
    time.sleep(1)
    counter-=1

print("Times Up !!!")
