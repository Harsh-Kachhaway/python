import random
import os
import time
number = int(random.random() * 100)

i = 1
while i > -1:
    guessed = int(input("guess the number"))
    if number > guessed :
        print("number is greter")
    elif number < guessed:

        print("number is smaller")
    elif number == guessed:

        print("you win")
        break
        time.sleep(2)
    i += 1
    time.sleep(2)
    os.system('cls')
print("you took " + str(i) + "attempt")