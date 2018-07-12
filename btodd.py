n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
for i in range(a+1,b):
    if(i%2!=0):
        print(i,end=" ")
