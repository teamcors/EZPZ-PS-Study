n,m = map(int,input().split())
count=0
while n!=m:
    if n>m: 
        count=-2 
        break
    elif str(m)[-1]=='1':
        m=m//10
        count+=1
    elif m%2==0:
        m=m//2
        count+=1
    else:
        count=-2
        break
print(count+1)
