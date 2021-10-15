import random
import time
p1 = 0
p2 = 0

while True:
    number = random.randint(1 , 100)
    player1 = int(input(" player 1 pick a number between 1 and 100 "))
    player2 = int(input(" player 2 pick a number between 1 and 100 "))
    print(" the number was " , number)
    if player1 > number and player2 > number :
         player1 - number < player2 - number
         p2 +=1
         print(" player 2 got a point the scores are \n " , p1 , p2 )
    elif player1 > number and player2 > number :
        player1 - number > player2 - number
        p2 +=1
        print(" player 2 got a point the scores are \n " , p1 , p2)
    elif player1 < number and player2 < number :
        number - player1 > number - player2
        p1 +=1
        print(" player 1 got a point the scores are \n " , p1 , p2)
    elif player1 < number and player2 < number :
        number - player1 < number - player2
        p2 +=1
        print(" player 2 got a point the scores are \n " , p1 , p2)
    elif player1 < number and player2 > number :
        number - player1 < player2 - number
        p1 +=1
        print(" player 1 got a point the scores are \n " , p1 , p2)
    elif player1 < number and player2 > number:
        number - player1 > player2 - number
        p2 +=1
        print(" player 2 got a point the scores are \n " , p1 , p2)
    elif player1 > number and player2 < number:
        player1 - number < number - player2
        p1 +=1
        print(" player 1 got a point the scores are \n " , p1 , p2)
    elif player1 > number and player2 < number :
        player1 - number > number - player2
        p2 +=1
        print(" player 2 got a point the scores are \n " , p1 , p2)
    elif player1 < number and player2 < number :
        number - player1 == number - player2
        print(" it's a tie the scores are \n " , p1 , p2)
    elif player1 == number and player2 != number :
        p1 +=2
        print("player 1 got two points the scores are \n " , p1 , p2)
    elif player1 != number and player2 == number :
        p2 +=2
        print("player 2 got two points the scores are \n " , p1 , p2)
    elif player1 < number and player2 > number :
        number - player1 == player2 - number
        print("it's a tie the scores are \n " , p1 , p2)
    elif player1 > number and player2 < number :
        player1 - number == number - player2
        print("it's a tie the scores are \n " , p1 , p2)
    #elif player1 != int :
        #p2 +=1
        #print ("player 2 got a point because player 1 is stupid \n " , p1 , p2)
    #elif player2 != int :
        #p1 +=1
        #print("player 1 got a point beacause player 2 is stupid \n " , p1 , p2)

