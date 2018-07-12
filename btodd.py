n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
li=[]
for i in range(a+1,b):
    if(i%2!=0):
        li.append(i)
for i in range(0,len(li)-1):
    print(li[i],end=" ")
print(li[i+1])
