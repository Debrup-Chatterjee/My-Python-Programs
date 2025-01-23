s="INDIA"

print("Pattern 1:")
for i in range(len(s)):
     print(s[0:i+1])

print("\nPattern 2:")
for i in range(len(s)-1,-1,-1):
     print(s[0:i+1])

print("\nPattern 3:")
for i in range(len(s)):
     print(s[i:])

print("\nPattern 4:")
for i in range(len(s)):
     print(s[i]*(i+1))

print("\nPattern 5:")
n=1
i=65
while(i<75):
     for j in range(i,i+n):
          print(chr(j),end="")
     i=i+n
     n=n+1
     print()

print("\nPattern 6:")
for i in range(len(s)):
     print(" "*(len(s)-(i+1))+s[0:i+1])