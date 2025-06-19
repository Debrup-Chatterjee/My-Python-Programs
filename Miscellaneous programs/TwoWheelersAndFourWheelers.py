'''An automobile company manufactures both two-wheelers(TW) and four-wheelers(FW).A comapnay manager wants
to make the prodcution of both the types of vehicles according to the given data below:
Total number of vehicles(two wheeler + four wheeler)= V
Total number of wheels= W
The task is to find how many two-wheelers and four wheelers need to be manufactured as per the given data:
eg: Input: V=200 , W=540
    Output: TW=130 , FW=70
    Explanation: 
    130+70=200
    (70*4)+(130*2)=540 wheels
    Constraints:
    2 <= W
    W % 2 = 0
    V < W
    Print "INVALID INPUT" if inputs do not meet the constraints. '''
    
v=int(input("Enter number of vehicles: "))
w=int(input("Enter number of wheels: "))
if w<2 or w%2!=0 or v>w:
     exit("INVALID INPUT")
tw=(4*v-w)//2
fw=v-tw
print(f"Two Wheelers = {tw} \nFour Wheelers = {fw}")
