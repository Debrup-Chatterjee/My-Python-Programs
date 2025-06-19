class Father:
     def __init__(self,property=0):
          self.property=property
     def display_property(self):
          print('Father\'s property= ',self.property)
class Son(Father):
     def __init__(self,property1=0,property=0):
          super().__init__(property)
          self.property1=property1
     def display_property(self):
          # accessing Father class's instance variable property
          print('Total property of the child= ',self.property1+self.property)
s=Son(200000.00,800000.00)
s.display_property()