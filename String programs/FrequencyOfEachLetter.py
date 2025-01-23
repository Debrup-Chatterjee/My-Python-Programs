s=(input("Enter a string: "))

#Printing frequency of each character in sorted manner
a=sorted(set(s))
d={i:s.count(i) for i in a}
print("Frequency of each character in the string:\n",str(d).replace("{","").replace("}","").replace(",","\n"))

#Finding characters with highest frequency
max_val=max(d.values())
l=[key for key,value in d.items() if value==max_val]
print("\nThe highest occuring  characters is/are:")
print(str(l).replace("[","").replace("]"," ").replace(","," and ") , "with frequency ",max_val)