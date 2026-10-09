s=input("enter a string")
v=0
c=0
n=0
sp=0
for i in s:
    if i in "aeiouAEIOU":
        v=v+1
    elif i.isalpha():
        c=c+1
    elif i.isdigit():
        n=n+1
    else:
        sp=sp+1
print("vowels=",v)
print("consonats=",c)
print("numbers==",n)
print("special characters=",sp)