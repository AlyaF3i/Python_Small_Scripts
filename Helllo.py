import random

outOf=int(input("The Rock paper scissor game is out of? "))

player=0
computer=0

possibility=("rock", "paper", "scissor")
while True:
    inputUser=str(input("Rock, Paper, Scissor: ")).lower()
    index=random.randint(0,2)
    inputComputer=possibility[index]
    print(f"\nYour choice: {inputUser}\n\nThe Computer Choice: {inputComputer}\n\n")
    if inputUser==inputComputer:
        print("No one got a point")
    elif inputComputer==possibility[0] and inputUser==possibility[1] or (inputComputer==possibility[2] and inputUser==possibility[0]) or (inputComputer==possibility[1] and inputUser==possibility[2]):
        print("You got a point")
        player+=1
    elif (inputComputer==possibility[1] and inputUser==possibility[0]) or (inputComputer==possibility[0] and inputUser==possibility[2]) or (inputComputer==possibility[2] and inputUser==possibility[1]):
        print("The Computer got a point")
        computer+=1
    else:
        print("Enter a right choice")
    print(f"Your Score: {player}\nComputer's Score: {computer}\n\n")
    
    if outOf==player:
        print("You won the game!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
        break
    if outOf==computer:
        print("you lose")
        break
    #ok then just without how many players
    #that's harder 
    #ok it's just always with 2 players 
    # no no if you pick if it's computer or players
    # ok
    # Yes
    # do you want another game?
    # but it would take longer to create
    # more writing 
    # so the computer willl have one of the word that was prepared before and we have to guess it
    # each time we guess wrong the computer will give us a hint
    # and the more hints he give the less marks we get "if we get it"
    # now the only thing would be hard is how long you will take to to write the hints and words
    # 4 <- 100 -> 75 -> 50 -> 25 -> 0
    # what game you said you will do?
    # ok so tomorrow it will be ready?
    # ok I will make one as well 

