import math
class Perfect:
     def __init__(self):
          self.start=int(input("Enter starting range: "))
          self.end=int(input("Enter ending range: "))
     @classmethod
     def isPerfectSquare(cls,n):
          return (int(math.sqrt(n))**2)==n
     def printRange(self):
          c=0
          print(f"The Perfect Squares from {self.start} and {self.end} are: ")
          for i in range(self.start,self.end+1):
               if Perfect.isPerfectSquare(i):
                    print(i)
                    c+=1
          if c==0:
               print("No Perfect Squares are present in the given range!")
ob1=Perfect()
ob1.printRange()
print(Perfect.isPerfectSquare(25))