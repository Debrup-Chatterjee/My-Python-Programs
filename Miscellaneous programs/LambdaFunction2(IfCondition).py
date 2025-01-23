l=[1,2,3,4,5]
l2=list(map(lambda x:x+1 if x%2==0 else x,l))
print(l2)