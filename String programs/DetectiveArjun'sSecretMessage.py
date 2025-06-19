'''In a small town, Detective Arjun is solving a case where a hacker has left a secret message.The message 
is a string where every alternate letter is part of the actual secret code.
Your task is to extract and print the secret code by picking every alternate character from the  given 
string, starting from index 0'''

s=input("Enter the string: ")
print("The secret message is: ",s[::2])