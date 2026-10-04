data=input()
data=data.split()
count=int(data[0])
sp=int(data[1])
cp=int(data[2])
storage=100
result=((sp-cp)*count-storage)
print(result)