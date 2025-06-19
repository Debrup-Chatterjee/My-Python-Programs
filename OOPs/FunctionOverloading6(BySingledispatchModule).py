from functools import singledispatch
import math
@singledispatch
def myfun(arg):
     print(f"Default: {arg}")
@myfun.register(int)
def _(arg):
     print(f"Integer: {arg}")
     print("Squared root: ",math.sqrt(arg))
@myfun.register(str)
def _(arg):
     print(f"String: {arg}")
     print(f"Length:{len(arg)}")
myfun(23.16)
myfun([10,25,35,5])
myfun("codehub")
'''@singledispatch decorator is used to mark the function under which the variation will be registered .
@myfun.register(type) decorator is used to mark the variations under the function myfun.
_ here is just a short cut name given to the functions as the function names do not matter in this case.
This is because the functions are registered under myfun therefore the variation function names do not
matter...We can give _,myfun,or even any other name to these functions if we want.'''