'''   The Lost Treasure Map
Story:
A group of explorers has found an ancient treasure map.The map consists of a string of letters and numbers,
but parts of it have been scrambled over time.
The treasure's location coordinates can be extracted from the map using this rule:
Extract all numbers from the string.Reverse their order(because the map is upside down).Return the sum of
these numbers.Your task is to decode the treasure location!
Input Format: A single  string S containing letters and digits(A-Z,a-z,0-9).
eg:
Input: "gold12silver34bronze56"
Output: 
     Numbers in the string: 12,34,56
     Reverse order: 56,34,12
     Sum: 56+34+12 = 102
Input: "diamond99ruby5pearl8"
Output: 
     Numbers in the string: 99,5,8
     Reverse order: 8,5,99
     Sum: 8+5+99 = 112'''

s=input("Enter the string: ")
if not(s.isalnum()):
     exit("INVALID INPUT")
if s[0].isdigit():
     l=[int(s[0])]
     c=0
else:
     l=[]
     c=-1
for i in range(1,len(s)):
     if s[i].isdigit():
          if s[i-1].isdigit():
               l[c]=l[c]*10+int(s[i])
          else:
               c+=1
               l.append(int(s[i]))
print("Numbers in the string: ",l)
print("Reverse order: ",l[::-1])
print("Sum: ",sum(l))
