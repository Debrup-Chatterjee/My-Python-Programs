class Base:
     def show(self):
          print("This is Code Hub Sodepur")

class Child(Base):
     def show(self):
          super().show()
          print("A computer programming centre")

c=Child()
c.show()