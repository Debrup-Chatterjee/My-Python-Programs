'''In the kingdom of Alphaland,a messenger lost one letter from a secret message.The message is given as
a shuffled string, but one letter is missing. Can you find the missing letter by comparing it with the
original unshuffled message?
eg: original string: banana
    shuffled string: nbana
    output: There is 1 a missing. '''

from collections import Counter
original=input("Enter original string: ")
shuffled=input("Enter shuffled string: ")
d1=dict(Counter(original)) # dictionary of original string
d2=dict(Counter(shuffled)) # dictionary of shuffled string
# Finding missing letters
for key,value in d1.items():
     if key not in d2:
          print(f"There is {d1[key]} '{key}' missing in the shuffled string.")
     elif d1[key]>d2[key]:
          print(f"There is {d1[key]-d2[key]} '{key}' missing in the shuffled string.")
