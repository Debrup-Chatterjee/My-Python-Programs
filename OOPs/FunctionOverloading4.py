class check_pal:
     def check(self,val=None):
          if val is None:
               print("No input is present")
          else:
               value=str(val)
               if value==value[::-1]:
                    print(f"'{val}' is a palindrome")
               else:
                    print(f"'{val}' is not a palindrome")
obj=check_pal()
num=int(input("Enter number: "))
st=input("Enter string: ")
obj.check()
obj.check(num)
obj.check(st)
