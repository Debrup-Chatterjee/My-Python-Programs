def myfun(a):
     if a%2==0:
          return True
     else:
          return False
arr=['A','x','Y','7','6','M']
arr1=filter(str.isalpha,arr)#Here str is an abstract string object
print(list(arr1))

arr2=[6,8,5,18,27,25]
arr3=filter(myfun,arr2)
print(list(arr3))

arr4=(5,1,6,4,8,11,3,12)
arr5=list(filter(lambda x:(x%2==0),arr4))
print(arr5)