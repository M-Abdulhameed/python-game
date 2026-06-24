import random
def easy():
    attempts=0
    number=random.randint(1,10)
    try:
        while True:
            guess = int(input(f'guess a number between 1 to 10:'))
            attempts+=1
            if guess > number:
               print("too high")
            elif guess < number:
               print("too low")
            elif guess == number:
               print(f'congratulations! you guessed the number in {attempts} attempts')
               break
    except ValueError:
        print("invalid input. please enter a valid number")
        easy()
def medium():
    attempts=0
    number=random.randint(1,50)
    print("you have 5 attempts to guess this number")
    try:
        for i in range(5):
            guess = int(input("guess a number between 1 to 50:"))
            attempts+=1
            if guess == number:
               print(f'congratulations! you guessed the number in {attempts} attempts')
               break
            elif guess > number:
               print("too high")
            elif guess < number:
               print("too low")
            if attempts==5:
               print(f" Failed!!, you have used all your attempts. The number was {number}")
    except ValueError:
        print('invalid input. please enter a valid number')
        medium()

def hard():
    attempts=0
    number=random.randint(1,100)
    print("you have 3 attempts to guess this number")
    try:
        for i in range(3):
            guess = int(input("guess a number between 1 to 100:"))
            attempts+=1
            if guess > number:
               print("too high")
            elif guess < number:
               print("too low")
            elif guess == number:
               print(f'congratulations! you guessed the number in {attempts} attempts')
               break
            if attempts==3:
               print(f" Failed!!, you have used all your attempts. The number was {number}")
    except ValueError:
        print('invalid input. please enter a valid number')
        hard()


def mode():
    while True:
        select = input("select difficulty level : Easy/Medium/Hard:").lower()
        if select == "easy":
            easy()
            break
        elif select == "medium":
            medium()
            break
        elif select == "hard":
            hard()
            break
        else:
            print("please select a valid difficulty level")
    again = input("want to play again yes or no :").lower()
    if again == "yes":
        mode()
    elif again == "no":
        print("thanks for playing!")
    else:
        print("invalid input,exiting the game")
mode()