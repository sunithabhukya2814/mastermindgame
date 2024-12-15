import random

# Function to generate a random 4-digit code
def generate_code():
   return [random.randint(0, 9) for _ in range(4)]

# Function to compare the guess with the code
def check_guess(code, guess):
   bulls = sum([1 for i in range(4) if code[i] == guess[i]])
   cows = sum([1 for i in range(4) if guess[i] in code and code[i] != guess[i]])
   return bulls, cows

# Main game loop
def mastermind_basic():
   code = generate_code()
   attempts = 10
   print("Welcome to Mastermind!")
   print("Guess the 4-digit code. You have 10 attempts.")

   while attempts > 0:
      guess = list(map(int, input("Enter your guess: ").strip()))
      bulls, cows = check_guess(code, guess)
      print(f"Bulls: {bulls}, Cows: {cows}")

      if bulls == 4:
         print("Congratulations! You've cracked the code!")
         break
      attempts -= 1

      if attempts == 0:
         print(f"Game Over! The code was: {''.join(map(str, code))}")

# Run the basic game
mastermind_basic()