from functools import reduce
l=[1,4,3,5,2]
maximum=reduce(lambda x,y:x if x>y else y,l)
minimum=reduce(lambda x,y:x if x<y else y,l)
print("The maximum number is {maximum}\nThe minimum number is {minimum}")