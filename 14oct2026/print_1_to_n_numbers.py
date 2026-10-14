def print_1ton(n):
    if n == 0:
        print_1ton(n-1)
        print(n,end=" ")  
    return
n=423234
print_1ton(n)