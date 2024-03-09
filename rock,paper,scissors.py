import random
#options in game
options=["Rock","Paper","Scissors"]
#get user input
user_choice=input("Enter a choice (Rock, Paper, Scissors): ").lower()
#computer choice
computer_choice=random.choice(options)
if(user_choice==computer_choice):
  print("It's a tie")
elif((user_choice=="rock" and computer_choice=="scissors") or(user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper") ):
  print("You win")
else:
  print("Computer wins")
