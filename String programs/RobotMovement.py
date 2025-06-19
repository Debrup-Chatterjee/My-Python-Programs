'''A robot is moving in a 2D grid starting from (0,0).It receives a sequence of moves:
"U" : move up
"D" : move down
"L" : move left
"R" : move right
Find the final position of the robot after all moves.
eg: Input:"UUDDLR"
    Output: (0,0) '''
s=input("Enter the movements: ")
l=[0,0] #initial position
for i in s:
     if i=="U" or i=="u":
          l[1]=l[1]+1
     elif i=="D" or i=="d":
          l[1]=l[1]-1
     elif i=="L" or i=="l":
          l[0]=l[0]-1
     elif i=="R" or i=="r":
          l[0]=l[0]+1
print("The final position of the robot is: ",tuple(l))