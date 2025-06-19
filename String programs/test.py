def longestPalindrome(s: str) -> str:
     if len(s)==1 or len(s)>1000 or s==s[::-1]:
          return s
     for i in range(0,len(s)-1):
          for j in range(len(s)-1,i,-1):
               if is_palindrome(s,i,j):
                    return s[i:j]
def is_palindrome(s,i,j):
     x=s[i:j]
     if x==x[::-1]:
          return True
     else:
          return False
print(longestPalindrome("cbbd"))