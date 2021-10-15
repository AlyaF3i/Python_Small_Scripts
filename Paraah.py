from random import randint
import time


num=int(input("Enter How many players: "))
players=[0 for a in range(num)]
playersname=[]
for a in range(1,num+1):
    playersname.append(input(f"\nEnter player {a} name: "))
def printScore():
    print()
    for name,score in zip(playersname,players):
        print(f"{name}: {score}")
    else:
        print()

OutOf=int(input("\nThe game is out of? "))
def CheckWinner():
    for ind,a in enumerate(players):
        if a==OutOf:
            return ind
    return -1

Max=int(input("\nGuessing Numbers up to? "))
guesses=[0 for a in range(num)]
while True:
    computerGuess=randint(0,Max)
    for i in range(num):
        guesses[i]=abs(int(input(f"\n{playersname[i]} Guess is: "))-computerGuess)
    winner=guesses.index(min(guesses))

    print(f"\nComputer guess was: {computerGuess}")
    time.sleep(1)
    print(f"\n{playersname[winner]} won")
    players[winner]+=1

    printScore()
    won=CheckWinner()
    if won!=-1:
        print(f"\n{playersname[won]} Has won!!!!")
        break
