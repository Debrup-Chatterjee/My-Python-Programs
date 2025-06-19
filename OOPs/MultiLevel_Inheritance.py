class Super:
     def square(self,a):
          return a*a

class Child(Super):
     def cube(self,a):
          return a**3
     
class Minichild(Child):
     def power(self,a,b):
          return a**b
     
obj=Minichild()
print(obj.square(5))
print(obj.cube(3))
print(obj.power(4,3))