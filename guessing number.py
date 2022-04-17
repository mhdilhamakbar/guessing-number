import random

# number_list = list(range(1,101))


number_list= random.choice(range(1,101))



def hard():
  print(number_list)
  # guess_right = False
  # while not guess_right :
 
 
  lives = 5
  while lives != 0:
    guess = int(input("Make a guess:"))
    if guess > number_list:
      print("Too high")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've ran out of life, you lose")
      
    elif guess < number_list:
      print("Guess again")
      print("Too low")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've ran out of life, you lose")

    elif guess == number_list:
      lives = 0
      print("Your guess is right")
   
   
  
    



  

def easy():
  lives = 10
  while lives != 0:
    guess = int(input("Make a guess:"))
    
    
    
    if guess > number_list:
      print("Too high")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've ran out of life, you lose")

      
    elif guess < number_list:
      print("Guess again")
      print("Too low")
      lives -= 1
      print(f"You have {lives} attempts remaining to guess the number")
      if lives == 0:
        print("You've ran out of life, you lose")


    elif guess == number_list:
      lives = 0
      print("Your guess is right")
   
   

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number_list}")
level = input("Choose a difficulty. Type 'easy' or 'hard':" )


if level == "easy":
  print("You have 10 attempts remaining to guess the number.")
  easy()
elif level == "hard":
  print("You have 5 attempts remaining to guess the number.")
  hard()

