print("-----Welcome to the Guessing Game-----")

import random
n = random.randint(1, 100)
guesses = 1
a = -1
while(a != n):
    a = int(input("Guess the number : "))
    if(a>n):
        print("Lower number please...")
        guesses += 1
    elif(a<n):
        print("Higher number please...")
        guesses += 1
print(f"You've guessed the number {n} correctly in {guesses} attemps")

