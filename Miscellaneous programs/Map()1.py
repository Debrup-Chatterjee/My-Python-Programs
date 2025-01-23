num=(2,3,1,4,5)
res=map(lambda x: x*x,num)#Using map() to change the values of a single iterable object
print(res)
print(list(res))
print(set(res))#This gives no output as once the map object is casted to one data type,the map object 
#cannot be used again.

num1=[2,3,1,4,5,6,7,8]
num2=[5,10,20,30]
res=map(lambda n1,n2: n1+n2,num1,num2)#Using map() to map the values into one iterable object from two 
#iterable data types
print(list(res))