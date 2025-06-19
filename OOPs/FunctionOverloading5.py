def myfun(val):
     if isinstance(val,int):
          print(f"You passed integer: {val}")
     elif isinstance(val,str):
          print(f"You passed string: {val}")
     elif isinstance(val,float):
          print(f"You passed float: {val}")
     else:
          print(f"Invalid type: {type(val)}")
myfun(15)
myfun("India")
myfun(67.45)
myfun([2,6,7])
# isinstance(val,int) checks if val is of int type...we can do this by writing type(val)==int also