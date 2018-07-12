n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
flag=0
li=[]
for i in range(a+1,b):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            li.append(i)
if (len(li)!=1):
    for i in range(0,len(li)-1):
        print(li[i],end=" ")
    print(li[i+1])
else:
    for i in range(0,len(li)):
        print(li[i])
