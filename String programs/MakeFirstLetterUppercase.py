s=input("Enter a sentence: ")
l=[w[0].upper()+w[1:] for w in s.split()]
print("Output: "," ".join(l))
