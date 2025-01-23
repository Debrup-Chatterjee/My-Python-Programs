fo=open("E:/My Python programs/File programs/sentences.txt","w")
# Taking sentences as input from user, until the user enters "END" or places "END" at the end of a sentence
while(True): 
     s=input("Enter a string or sentence(Enter END to quit): ")
     if(s=="END"): # User eneters just "END" as input sentence
          break
     elif(s.endswith("END")): # END is present at the end of a input sentence
          fo.write(s[:-3]+"\n")
          break
     else:
          fo.write(s+"\n")

fo=open("E:/My Python programs/File programs/sentences.txt","r")
s=fo.readlines() # list of all sentences
s=list(filter(lambda x:x[0].isupper(),s)) # list of sentences beginning with Uppercase alphabet
print("The list of sentences that begin with an uppercase alphabet are:")
if(len(s)==0):
     print("No senetences beginning with Uppercase letter are present !")
else:
     print(s)
fo.close()