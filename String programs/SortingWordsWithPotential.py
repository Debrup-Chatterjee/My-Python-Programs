def potential(w):
    return sum([ord(i) for i in w])
s=input("Enter a sentence: ")
l=sorted(s.split(),key=potential)
print("Words sorted according to potential:\n"," ".join(l))
print("Word with the highest potential: ",l[-1])