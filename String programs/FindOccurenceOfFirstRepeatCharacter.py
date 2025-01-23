s=input("Enter a string: ")
f=list(filter(lambda a:(s.count(a)>1),s))#List of repeat characters in the list
if(len(f)==0):
     print("No repeat characters are present")
else:
     x=sorted(f,key=s.index)#Sorting the repeat characters acccroding to their occurence index
     print("The first repeated character is ",x[0])