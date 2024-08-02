import random
import time
def game():
    randno = random.randint(1,3)
    player1 = None
    player2 = input("plqyer:enter your input:")

    if randno == 1:
        player1 = 'r'
    elif randno == 2:
        player1 = 'p'
    elif randno == 3:
        player1 = 's'

    if player1 == player2:
        print("draw")
    elif player1 == 'r' and player2 == 'p':
        print("player2 wins ")
    elif player1 == 'r' and player2 == 's':
        print("com wins ")
    elif player1 == 'p' and player2 == 's':
        print("player2 wins ")
    elif player1 == 'p' and player2 == 'r':
        print("com wins ")
    elif player1 == 's' and player2 == 'r':
        print("player2 wins ")
    elif player1 == 's' and player2 == 'p':
        print("com wins ")
    else:
        print("error")
    print("thank your")
    time.sleep(2)
    game()
game()

