from random import randint
import sys

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n > 0:
        rand = randint(1,n)
        while True:
            try:
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess < 0:
                continue
            elif guess > rand:
                print("Too large!")
            elif guess < rand:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit()
