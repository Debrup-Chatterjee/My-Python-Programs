class Dudeney:
     def __init__(self):
          self.start=int(input("Enter starting range: "))
          self.end=int(input("Enter ending range: "))
     def isDudeney(self,n):
          a=n
          sum=0
          while(a!=0):
               sum+=a%10
               a=a//10
          return (sum**3)==n
     def printRange(self):
          c=0
          print(f"The Dewdenny numbers from {self.start} and {self.end} are: ")
          for i in range(self.start,self.end+1):
               if self.isDudeney(i):
                    print(i)
                    c+=1
          if c==0:
               print("No Dudeney numbers are present in the given range!")
ob1=Dudeney()
ob1.printRange()