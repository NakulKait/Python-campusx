import random
jackpot = random.randint(1,100)
guess = int(input("Guess the number between 1 to 100 :"))
counter = 1
while guess != jackpot :
    if jackpot > guess :
        print("Guess Higher ")
    else:
        print("Guess Lower ")
    guess = int(input("Guess the number between 1 to 100: "))
    counter += 1

print("You guessed correctly .")

print("You took" , counter , "to guess correctly.")
