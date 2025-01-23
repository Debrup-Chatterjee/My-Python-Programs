l=[2,4,7,2,7,3,9,3]
d={}
for i in l:
     if i not in d:
          d[i]=1
     else:
          d[i]+=1
print("The frequency of each element is:")
for k,v in d.items():
     print(k,"=",v)