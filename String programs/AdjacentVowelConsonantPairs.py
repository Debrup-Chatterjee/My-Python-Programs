'''Count the number of adjacent vowel-consonant pairs in a given string.'''
import re
s=input("Enter a string: ")
pat=r"[aeiou][^aeiou]" # Consecutive vowel-consonant pairs
mat=re.findall(pat,s) # Finding all matches
print("Adjacent vowel-consonant pairs are : ",mat)