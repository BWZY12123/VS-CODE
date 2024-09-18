#Guessing numbers game
import random

num = random.randint(1,100)



while True:
  guess = int(input("Please enter an integer within one hundred："))
  if guess == num:
      print("You're a good guy")
      break
  elif guess > num:
      print("Don't be so radical, be a little smaller")
  else:
      print("Too conservative, a little bigger")
    