n=int(input())
sum=0
temp=n
while(n!=0):
    ans=n%10
    res=pow(ans,3)
    sum=sum+res
    n=round(n//10)
if(temp==sum):
    print("yes")
else:
    print("no")
    
