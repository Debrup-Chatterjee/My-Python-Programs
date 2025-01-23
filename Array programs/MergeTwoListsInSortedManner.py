l1=[4,8,8,9,11]
l2=[3,7,9]
i=0
j=0
while i<len(l1) and j<len(l2):
     if l1[i]>l2[j]:
          l1.insert(i,l2[j])
          j=j+1
     else:
          i=i+1
l1=l1+l2[j:]
print(l1)