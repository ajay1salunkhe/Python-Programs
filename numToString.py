
print("\nEnter starting range : ",end="")
start=int(input())
print("\nEnter ending range : ",end="")
end=int(input())

string=""

for i in range(start,end+1):
    string+=str(i)

print(string)
