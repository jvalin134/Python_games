def add(a,b,c):
   return a + b + c
def sumall(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k):
    return q+w+e+r+t+y+u+i+o+p+a+s+d+f+g+h+j+k
def printbored() :
    # zero = if xstate: print("X") else(if ostate: print("O") else ) --> this is wrong way to write 
    zero = "x" if xstate[0] else("O" if ostate[0] else 0)
    one = "x" if xstate[1] else("O" if ostate[1] else 1)
    two = "x" if xstate[2] else("O" if ostate[2] else 2)
    three = "x" if xstate[3] else("O" if ostate[3] else 3)
    four= "x" if xstate[4] else("O" if ostate[4] else 4)
    five = "x" if xstate[5] else("O" if ostate[5] else 5)
    six = "x" if xstate[6] else("O" if ostate[6] else 6)
    seven = "x" if xstate[7] else("O" if ostate[7] else 7)
    eight = "x" if xstate[8] else("O" if ostate[8] else 8)

   
    print(f"{zero} | {one} | {two}")
    print(f"----------")
    print(f"{three} | {four} | {five}")
    print(f"----------")
    print(f"{six} | {seven} | {eight}") 

def checkwin(xstate,ostate) :
   wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
   for win in wins: # -->  "For each win in wins" (OR) Go through all the items in wins, one by one, and call each item win 
        if(add(xstate[win[0]] , xstate[win[1]] ,xstate[win[2]]) == 3):
           printbored()
           print("X won !!")
           return 1
        elif(add(ostate[win[0]] , ostate[win[1]] ,ostate[win[2]]) == 3):
            printbored()
            print("O won !!")
            return 0
   if(sumall(xstate[0],xstate[1],xstate[2],xstate[3],xstate[4],xstate[5],xstate[6],xstate[7],xstate[8],ostate[0],ostate[1],ostate[2],ostate[3],ostate[4],ostate[5],ostate[6],ostate[7],ostate[8]) == 9):
            print("D R A W")
            return 2
# a better way to do the Draw in python is :
#    if(sum(xstate) + sum(ostate) == 9): # ---> sum is a built in fuction in python which add all the value in the list 
#         print("D R A W")
#         return 2
   else:
       return -1
           
           
           
      


xstate = [0,0,0,0,0,0,0,0,0] # --> this are list 
ostate = [0,0,0,0,0,0,0,0,0] 
print("Welcome to tik tac toe")
turn = 1
while True:
    printbored()
    if (turn == 1):
        print("X's Turn")
        value = int(input("pick a number "))
        xstate[value] = 1 # --> we are assigning 1 on the location of the number we input in the list 
                       # --> ex :- input = 3 , xstate[3] = 1 --> xstate = [0,0,0,3,0,0,0,0,0]
    else:
        print("O's Turn")
        value= int(input("pick a number "))
        ostate[value] = 1
    cwin = checkwin(xstate,ostate)

    if(cwin != -1):
        
        print("Match over")
        break
    
    
    turn = 1 - turn 

    

     


