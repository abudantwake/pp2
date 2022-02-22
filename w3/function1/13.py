import random
def g():
    tries = 0
    number = random.randrange(1 , 20)

    name = input("Hello! What is your name?\n")

    firsttxt = "Well, {}, I am thinking of a number between 1 and 20.\nTake a guess."
    wrongtxt = "Your guess is too {}.\nTake a guess."
    endtxt = "Good job, {}! You guessed my number in {} guesses!"
    print(firsttxt.format(name))

    while True:
        inum = int(input())
        if inum == number:
            print(endtxt.format(name , tries))
            break
        else:
            tries += 1
            if inum > number:
                print(wrongtxt.format("big"))
            else:
                print(wrongtxt.format("low"))
