import random
is_on = True

while (is_on == True):
    solution = random.randint(0, 10)
    guess = int(input("Guess the number I'm thinking of between 0 and 10: "))
    while (guess != solution):
        if guess < solution:
            print(f"Sorry! The number on my mind is larger than {guess}.")
        elif guess > solution:
            print(f"Sorry! The number on my mind is smaller than {guess}.")
        guess = int(input("Guess another number: "))
    if (guess == solution):
        print(f"Congratulations! {guess} is exactly what I was thinking of!")
    restart = input("Do you want to play again? ")
    if restart == "no":
        is_on = False