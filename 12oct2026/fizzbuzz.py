count=int(input("enter a number"))
output=[]
for i in range(1,count+1):
    if i % 3 == 0:
        if i % 5 == 0:
            output.append("fizzbuzz")
        else:
            output.append("fizz")
    elif i % 5 == 0:
        output.append("buzz")
    else:
        output.append(i)
print(output)
