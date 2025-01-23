import re
match=re.search(r'world','Hello world like World')
print(match.group())
print(match.start())# starting index of the word
print(match.end())# ending the index of the word
print(match.span())# starting and ending index of the word