import random

def game():

    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 3:
        try:
            guess = int(input("Give me a number! "))
        except ValueError:
            guess = str()
            print("{} isn't a number".format(guess))
        else:
            if guess == secret_num:
                print("You got it!. the number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
        guesses.append(guess)
    else:
        print("You didn't get it! my number was {}".format(secret_num))
    play_again = input("Do you want play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")
game()
