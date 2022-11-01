from random import randint
#create a list of play options
t = ("rock ", "paper ", "scissors ")

#assign a random play to the computer
computer = t[randint(0,2)]
#User name 
user = input("enter your name? ")

print("\nWell Hello, " + str(user) + " How are you \n")

print("please pick one of the following. " )

#set player to False
player = False

#Set player to true
while player == False:

    player = input("rock, paper, scissors ")
    if player == computer:
        print(str(user) + " It was a TIE, no one wins or loses")
    
    elif player == "rock":
        if computer == "paper":
            print("paper covers rock you lose " + str(user))
        else: 
            print("rock smashes scissors you win " + str(user)) 
   
    elif player == "paper":
        if computer == "scissors":
            print("you lost " + str(user) + " scissors cuts paper")
        else:
            print("You win " + str(user) + " paper covers rock")
    
    elif player == "scissors":
        if computer == "rock":
            print("you lose " + str(user) + " rock crushes scissors")
        else:
            print("you win " + str(user) + " scissors cut paper")
    else: 
        print("That's not a valid play... Please check your spelling")

    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
