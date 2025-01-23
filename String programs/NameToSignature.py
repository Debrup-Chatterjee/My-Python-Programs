s=input("Enter your name: ").split()
print("Your Signature is: ",".".join([w[0].upper() for w in s[:-1]])+ "." +s[-1].capitalize())