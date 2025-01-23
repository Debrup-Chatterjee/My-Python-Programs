from collections import Counter
l=[11,11,11,22,22,22,33,44,44]
freq=Counter(l)
print("The frequency of elements are: ")
print(str(freq).replace('Counter({','').replace('})','').replace(':','='))

#Same thing but without using Counter,but there is an internal loop while creating the dictionary
print("The frequency of each element is:")
d={num:l.count(num) for num in set(l)}
print(d)

#Finding all the keys with the maximum value
max_val=max(d.values())
max_keys=[key for key,value in d.items() if value==max_val]
print("The elements with the highest frequency are:")
print(str(max_keys).replace('[','').replace(']','') , ' with frequency ' ,max_val)

#A function to sort the dictionary according to values and return the list of keys
print(sorted(d,key=d.get))