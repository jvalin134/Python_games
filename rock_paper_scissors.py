import random
def computer_choice(rps):
    c_choice = random.choice(rps)
    print(f"computer choice -> {c_choice}")
    return c_choice

def human_choice():
    h_choice = input("Enter(rock or paper or scissor): ")
    if h_choice.lower() != "rock" and h_choice.lower() != "paper" and h_choice.lower() != "scissor":  # better way --> if h_choice not in ["rock", "paper", "scissor"]:
                                                                                                      #                     return "error "                              
        return "error"
    else:
        return h_choice.lower()

def points(a,b):
    if a == b :
        print("no one's point")
    elif a == "error" :
        print("WRONG SPELLING")
        return "no_point"
    elif a == "rock" and b == "paper" :
        print("Computer's point")
        return "computer"
    elif a == "paper" and b == "scissor":
        print("Computer's point")
        return "computer"
    elif a == "scissor" and b == "rock":
        print("Computer's point")
        return "computer"
    else:
        print("Your point")
        return "human"
        
   
    

rps = ["rock","paper","scissor"]

print("############## WELCOME TO ROCK PAPER SCISSORS WITH PYTHON ##############")
print ("#############  Whoever win the maximum points will WIN !! ############## ")

human_score = 0 
computer_score = 0

for i in range(7):
    print("-" * 40)
    print(f"     ROUND *{i + 1}*    ")
    print("-" * 40)
    human_return = human_choice()
    computer_return = computer_choice(rps)
    winner = points(human_return,computer_return)
    if winner == "human":
        human_score += 1
    elif winner == "computer":
        computer_score += 1
    else:
        human_score += 0
    print(f"Score: you -> {human_score} , computer -> {computer_score}")    
print("!!!!!!!!!!!!!!! Final result !!!!!!!!!!!!!!!")
if human_score > computer_score :
    print("You WON ;) !!! ")
elif computer_score > human_score :
    print(" Computer WON :( ")
else :
    print(" It was a DRAW") 
    

    




