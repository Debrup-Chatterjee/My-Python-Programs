from functools import reduce
def add(a,b):
     return a+b
num=[1,2,3,4,6,7,8,9,10,12,5]
sum=reduce(add,num)
print(f"Sum of thhe integers of num list : {sum}\n")
sum=reduce(add,num,10)
print(f"Sum of the integers of num list with initial value 10 : {sum}\n")

num=[1,4,3,6,5,2]
prod=reduce(lambda x,y :x*y,num)
print(f"Product = {prod}")