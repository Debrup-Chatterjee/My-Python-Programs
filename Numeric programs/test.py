n=int(input())
l=list(map(int,input().split()))
s=list(set(l))
a=0
b=a+len(s)
m=sum(l)
flag=True
while a<n:
    for j in s:
        if j not in l[a:b+1]:
            flag=False
            break
        else:
            continue
    if flag==False:
        b=b+1
        flag=True
        continue
    else:
        if sum(l[a:b+1])<m:
            m=sum(l[a:b+1])
        a=a+1
        b=a+len(s)
print(m)
    
    