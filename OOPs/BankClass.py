class Bank:
     def __init__(self,name,balance=0.0):
          self.name=name
          self.balance=balance
     def deposit(self,amount):
          self.balance+=amount
          return self.balance
     def withdraw(self,amount):
          if amount>self.balance:
               print('Balance amount is less, so no withdraw.')
          else:
               self.balance-=amount
          return self.balance
     def display(self):
          return self.balance
name=input("Enter name: ")
b=Bank(name)
while(True):
     print("d -deposit, w- Withdraw, b- Display balance, e-Exit")
     choice=input("Enter choice: ")
     if choice=='e' or choice=='E':
          exit()
     elif choice=='b' or choice=='B':
          print("Current balance is ",b.display())
     elif choice=='d' or choice=='D':
          amt=float(input("Enter amount: "))
          print("Balance after deposit: ",b.deposit(amt))
     elif choice=='w' or choice=='W':
          amt=float(input("Enter amount: "))
          print("Balance after withdrawal: ",b.withdraw(amt))