from random import *
def dice():
        print "dice is rolling"
        x = randint(1,6)
        print "dice rolled %d",x
        return x
snake = {}
ladder = {}
i = 0 
while (i <6 ):
	x = randint(1,100)
	snake[x]=randint(5,20)
	i = i + 1
i = 0
while (i <6 ):
        x = randint(1,100)
	print "i am here with %d" %x
	if snake.has_key(x):
		continue
        ladder[x]=randint(5,20)
        i = i + 1
print snake
print ladder
print "Welcome to ladder and snake, the one who reaches the 100 will win"
print "Player-1 = 0 \nprint player-2 = 0 \n"
print "lets begin the game"
P1 = 0
P2 = 0
while (P1 < 100 and P2 < 100):
	print "snake is in ",snake
	print "ladder is in ",ladder
	print "player 1's chance " 
	while (1) :
		var = raw_input("please enter y to continue")
		if var == "y" :
			break 
	a = dice()
	P1 = P1 + a
	if P1 >= 100:
		print "Player 1 wins"
		exit();
	if snake.has_key(P1):
		print "player-1 is caught by snake in %d" %(P1)
		P1 = P1 - snake[P1]
        if ladder.has_key(P1):
                print "player-1 is in ladder in %d" %(P1)
                P1 = P1 + ladder[P1]
	print "player 2's chance "
	a = dice()
        P2 = P2 + a
        if P2 >= 100:
                print "Player 2 wins"
		exit();
        if snake.has_key(P2):
                print "player is caught by snake in %d" %(P2)
                P2 = P2 - snake[P2]
        if ladder.has_key(P2):
                print "player is caught by ladder in %d" %(P2)
                P2 = P2 + ladder[P2]


	print "P1 is in %d and P2 is in %d "  %(P1,P2)


