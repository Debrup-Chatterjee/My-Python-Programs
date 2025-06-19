'''The user gives an input list suppose [-1,1,-2,-3,-4,2,3,4,5,6] the output list will have positive and
negative numbers alternatively,i.e., output will be [1,-1,2,-2,3,-3,4,-4,5,6]
'''
l=[]
n=int(input("Enter how many numbers you want to enter: "))
if(n<=0):
     exit("Invalid choice of input...please enter a positive natural number !")
print(f"Enter {n} numbers into the list: ")
for i in range(0,n):
     x=int(input())
     l.append(x)
#Alternating numbers
neg=list(filter(lambda a:(a<0),l))# list of all negative numbers
pos=list(filter(lambda a:(a>=0),l))# list of all positive numbers
maxLen=neg if(len(neg)>len(pos)) else pos # list which has more length
l2=[]
result=list(map(lambda n1,n2:l2.extend([n1,n2]),pos,neg))
l2=l2+pos[len(neg):]+neg[len(pos):]# adding excess elements of bigger list
print("Output: ",l2)