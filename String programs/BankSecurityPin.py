'''A bank has a security system that generates a locker PIN based on a customer's name and birth year.
The PIN is generated as follows:
First character = First letter of the name(uppercase).
Second character = Last letter of the name(uppercase).
Third and Fourth characters = Sum of all digits in the birth year.
eg: Input: "Rohan",1995
    Output: "RN24" #(1+9+9+5=24)
'''
name=input("Enter your name: ")
name=name.strip()
year=input("Enter your year of birth: ")
if len(year)!=4 or year.isdigit()==False:
     exit("Invalid year entered")
sum=sum(list(map(lambda x:int(x),year)))
print("Your locker PIN is: ",name[0].upper()+name[-1].upper()+str(sum))