import time, random, csv
import time
player1 = ""
player2 = ""
rounds = 0
p1score = 0
p2score = 0
p1points = 0
p2points = 0
p1tiebreaker = 0
p2tiebreaker = 0
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
#global p1score
#global p2score


def createAccount(): #function to create the account
    username = input("please create your username? ") #input which asks for a username to create your account
    password = input("Please create your password? ") #input which asks for a password to create your account
    file = open("Accounts.txt", "a") #opens a text file in ammend mode
    file.write(str(username)+ "/" +(password))#writes the username and password you inputted into the text file
    file.write("\n") #adds a new line to the text file
    file.close() #closes the text file
    print("Account successfully made, you will now be sent back to the menu..") #prints out something at the end to notify the user the account was successfully made





def playGame(): #function to play the game
    p1name = input("What is your username player 1?")
    p2name = input("What is your username player 2?")
    print("Hello and welcome", p1name, "and hello and welcome", p2name)

    global p1score
    global p2score
    rounds = 0
    while rounds != 5: #while loop which plays the 5 rounds
        rounds = rounds + 1 #after each loop 1 will be added on to the variable 'rounds'
        print("\n It is round",(rounds)) #it will output the round you are currently on


        print("\n It is player 1's turn")

        input("Press 'R' to roll the dice:")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("You rolled the number", str(dice1),"and rolled the number",str(dice2),".")
        dicetotal = dice1 +dice2

        if dicetotal%2 == 0:
            print("You rolled an even number, 10 points have been added to your score!")
            p1score = (p1score + 10)
        else:   
            print("You rolled an odd number, 5 points were deducted from your score!")
            p1score = (p1score - 5)

        if dice1==dice2:
            print("You have rolled a double, an extra roll has been awarded!")
            input("Press 'R' to roll your extra dice!")
            dice3 = random.randint(1,6)
            print("/n You rolled the number",str(dice3),".")
            p1score = dice1+dice2+dice3
            if p1score<0:
                p1score = 0
            print("Your current score is",p1score,"\n")

        print("Your current score is:",p1score)
      


        print("\n It is player 2's turn!")
        input("Press 'R' to roll the dice:")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("You rolled the number", str(dice1),"and rolled the number",str(dice2),".")
        dicetotal = dice1 +dice2

        if dicetotal%2 == 0:
            print("You rolled an even number, 10 points have been added to your score!")
            p2score = (p2score + 10)
        else:   
            print("You rolled an odd number, 5 points were deducted from your score!")
            p2score = (p2score - 5)

        if dice1==dice2:
            print("/nYou have rolled a double, an extra roll has been awarded!")
            input("Press 'R' to roll your extra dice!")
            dice3 = random.randint(1,6)
            print("You rolled the number",str(dice3),".")
            p2score = dice1+dice2+dice3
            if p2score<0:
                p2score = 0
            print("Your current score is",p2score,"\n")

        print("Your current score is:",p2score)