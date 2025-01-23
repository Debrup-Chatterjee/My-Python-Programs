def swap(w):
     if(len(w)==1):
          return w
     else:
          return w[-1]+w[1:-1]+w[0]
s=input("Enter a sentence: ")
l=[swap(w) for w in s.split()]
print("Sentence after swapping first and last characters of each word:\n"," ".join(l))
