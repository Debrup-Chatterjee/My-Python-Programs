'''Instance methods are of two types: Accessor methods and Mutator methods.
Accessor methods simply access or read data of the variables.They do not modify the data in the variables.
Accessor methods are generally written in the form of getXXX() and hence they are also called Getter 
methods.
Mutator methods are the methods which not only read the data but also modify them.They are written in the
form of setXXX() and hence they are also called Setter methods.'''
class Student:
     #mutator method
     def setName(self,name):
          self.name=name
     #accessor method
     def getName(self):
          return self.name
     #mutator method
     def setMarks(self,marks):
          self.marks=marks
     #accessor method
     def getMarks(self):
          return self.marks
#create Student class instance
s=Student()
s.setName("Rahul")
s.setMarks(99)
print("Hi ",s.getName())
print("Your marks is ",s.getMarks)