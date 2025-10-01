import random

selected_value = random.randint(1, 20)

won = False

while not won:
    guess = int(input("Guess my number! "))
    if guess == selected_value:
        print("Wow! You won!")
        won = True
    elif guess < selected_value:
        print("My number is larger!")
    else:
        print("My number is smaller!")
