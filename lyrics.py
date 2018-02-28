#program which shows lyrics of song
import time
song=input("Enter song name : ")

s=open(song).read()

for c in s:
    print(c,end='',flush=True)
    time.sleep(0.07)
