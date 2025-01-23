def mygen(x,y): #our generator name is 'mygen'
     while x<=y:
          yield x
          x+=1
g=mygen(5,10)
print(g)#The generator function returns a generator  object
for i in g:
     print(i,end=",")
print()
#Once a element of a generator object is traversed, it cannot be traversed again hence this following loop
#is not executed
for x in g:
     print(x,end=",")
#We can also use the next() function to traverse a generator
g=mygen(5,18)
print(next(g))
print(next(g))
