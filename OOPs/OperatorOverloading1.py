class Complex:
     def __init__(self):
          self.real=0
          self.imag=0
     def setValue(self,real,imag):
          self.real=real
          self.imag=imag
     def __add__(self,C): # + operator overloaded
          Temp=Complex()
          Temp.real=self.real+C.real
          Temp.imag=self.imag+C.imag
          return Temp
     def display(self):
          print("(",self.real," + ",self.imag,"i)")
C1=Complex()
C1.setValue(1,2)
C2=Complex()
C2.setValue(3,4)
C3=Complex()
C3=C1+C2 # calls overloaded + opearator
print("Result = ",end="")
C3.display()
'''Operators and their corresponding overloading function
+ : __add__
- : __sub__
* : __mul__
/ : __div__
** : __pow__
% : __mod__
+= : __iadd__
-+ : __isub__
*= : __imul__
/= : __idiv__
**= : __ispow__
%= : __imod__
>> : __rshift__
& : __and__
| : __or__
^ : __xor__
~ : __invert__
<< : __lshift__
>>= : __irshift__
&= : __iand__
|= : __ior__
^= : __ixor__
~= : __iinvert__
<<= : __ilshift__
> : __gt__
< : __lt__
>= : __ge__
<= : __le__
== : __eq__
!= : __ne__
'''