'''Find Leftover Elements in a Range
Given a range [L,U] and an array A of N elements,find all numbers that are not present in A within the 
given range.The missing numbers should be grouped sequentially.
Input 1: 1 10 1 5
Output 1: [1 4][6 10]
Explanation: The first two numbers in the input is the given range(1 to 10).The third number is the length
of array(1).The fourth number 5 is the 1 array element.In output, [1 4] and [6 10] are the range of numbers
missing.
Input2: 3 90 5 7 22 50 66 78 
Output2: [3 6] [8 21] [23 49] [51 65] [67 77] [79 90]
'''
#Taking and dissecting input
l=list(map(int,input("Enter input: ").split()))
start=l[0]
end=l[1]
n=l[2]
l=l[3:]

# Finding the leftover elements from the range which are not present in the array in ascending order
leftover=sorted(list( set(range(start,end+1)) - set(l) ))
if len(leftover)==0:
     exit("No leftover elements are present from the range")
# Forming ranges of the leftover elements and storing it in 'a' to get the desired output
a=[]
b=[leftover[0]]
for i in range(1,len(leftover)):
     if leftover[i]!=leftover[i-1]+1:
          if b[0]!=leftover[i-1]:
               b.append(leftover[i-1])
          a.append(b)
          b=[leftover[i]]
     elif leftover[i]==leftover[i-1]+1:
          continue
if b[0]!=leftover[i]: # for including the last element of the leftover list
     b.append(leftover[i])
a.append(b)
# Printing the desired output
print("Output: ",a)