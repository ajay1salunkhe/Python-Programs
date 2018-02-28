

str="Ajay"

if "J" not in str:
    print("J is not present in string")

#indexing
print("str : ",str)
print("str[:2] : ",str[:2])
print("str[-1:] : ",str[-1:])
print("str[2:] : ",str[2:])
print("str[-3:-1] : ",str[-3:-1])
print("str[:] : ",str[:])
print("str[::2] : ",str[::2])
print("str[::-1] : ",str[::-1]) #reverses string
print("str[::-2] : ",str[::-2])

#python strings are immutable
#str[3]="x" will not work
print("\n str : ",str)
str=str[:3]+"x"+str[4:]
print("\n str after str=str[:3]+\"x\"+str[4:] : ",str)

#looping of strings
print("\nlooping of strings\n")

for i in range(len(str)):
    print("str[",i,"] : ",str[i])

for c in str:
    print(c)

print("\nString Methods : \n")

print("str.lower() : ",str.lower())
print("str.upper() : ",str.upper())
print("str.replace(\"x\",\"y\") : ",str.replace("x","y"))
print("str.count(\"a\") : ",str.count("a"))
print("str.index(\"A\") : ",str.index("A"))
print("str.isalpha() : ",str.isalpha())
print("str.capitalize() : ",str.capitalize())
print("capitalize() returns string with first character capitalize")
