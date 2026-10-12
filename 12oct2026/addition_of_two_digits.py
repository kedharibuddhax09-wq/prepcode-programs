number=int(input("eneter the number:"))
total=0
while number > 0:
    last = number % 10
    number = number // 10
    total = total+number
print(total)