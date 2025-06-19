'''A class method can access only class level attributes(class variables) of a class using the cls 
parameter.It cannot access the instance variables of a class.A class method works on class/static variables
of a class which are shared by all instances of a class.
These methods are written using the @classmethod decorator above them.By default,the first parameter for 
class methods is 'cls' which refers to the class itself.
A class method is called with class name like classname.method(), although we can also call the method by 
an object of the class like ob.method().
The processing which is commonly needed by all the instances of the class is handled by the class methods.
'''
class Bird:
     #this is a clas/static variable
     wings=2
     #this is a class method
     @classmethod
     def fly(cls,name):
          print('{} flies with {} wings'.format(name,cls.wings))
#display information for 2 birds
Bird.fly('Sparrow')
Bird.fly('Pigeon')
'''Here,we have developed a Bird class.All birds in the Nature have only 2 wings.So,we take 'wings' as a
class variable.Now a copy of this class variable is available to all the instances of Bird class.The class
method fly() can be called as Bird.fly() '''