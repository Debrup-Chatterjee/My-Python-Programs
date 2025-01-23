x="Python string"
print(x)
print("i. ",x.lower())#converts the entire string into lowercase
print("ii. ",x.upper())#converts the entire string into uppercase
print("iii. ",x.capitalize())#converts only the first letter of the string into uppercase and rest to lowercase
print("iv. ",x.title())#converts initial letter of each word to capital and rest of the letters to lowercase
print("v. ",x.swapcase())#converts all uppercase characters to lowercase and vice-versa

##
a="Anushka Bharati"
b="BHARATI542"
c="7551020886"
d="C"
print("1.",a)
print("2.",a.islower())#checks if all characters are lowercase or not
print("3.",b)
print("4.",b.isupper())#checks if all characters are uppercase or not
print("5.",a.istitle())#checks if the string is title cased( first letter of each word is capital and rest
# of the letters are lowercase)
print("6.",c)
print("7.",c.isdigit())#checks if all characters are digits or not
print("8.",a.isalpha())#checks if all characters are alphabets
print("9.",b.isalnum())#checks if all characters are alphabets or digits
print("10.",a.strip())#removes excess whitespaces from both side
print("11.",a.lstrip())#removes whitespaces from left side
print("12.",b.rstrip())#removes whitespaces from right side
print("13.",a.startswith("A"))#checks if the string starts with the parameter
print("14.",b.endswith("I"))#checks if the string ends with the parameter
print("15.",a.count("a"))#counts the paramter occurences from the string
print("16.",b.index("I"))#returns position of the first occurence of the character
print("17.",c.replace("1","E"))#replaces all occurences of the first parameter with the second parameter
print("18.",a.split())#splits the string into a list of items whenever a space occurs
print("19.",a.split(","))#splits the string into a list of items whenever a comma occurs
print("20.",ord(d))#converts the character into its ASCII code
print("21.",chr(65))#converts the ASCII code into its equivalent character

print("Split and Join functions:")
e="He is a good boy"
l=e.split()
print(l)
f=" hmm ".join(l)#concatenates all the items of a list and converts it to a string after adding a " hmm "
# between all elements of the list
print(f)

print("\nAccessing string characters like list:")
print(e[3])
print(e[3:12])

l=sorted(e)#sorts a string by ASCII values
print("String after sorting:", "".join(l))