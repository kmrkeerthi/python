n=input()
n=n.split()
n1=int(n[0])
key=int(n[1])
num=input()
num=num.split()
sum=0
for i in range(0,key):
    sum=sum+int(num[i])
print(sum)
