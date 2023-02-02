import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [Rock, Paper, Scissor]

user_pick = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor:\n"))

if user_pick >= 3 or user_pick < 0:
    print("You typed invalid number")
else:  
    computer_pick = random.randint(0, 2)
    print(f"You pick \n{options[user_pick]}")
    print(f"computer pick \n{options[computer_pick]}")
    if user_pick == computer_pick:
        print("It's draw")
    elif user_pick == 0 and computer_pick == 2:
        print("You win")
    elif user_pick == 2 and computer_pick == 1:
        print("You win")
    elif user_pick == 1 and computer_pick == 0:
        print("You win")
    elif len(options) != user_pick:
        print("Invalid number")
    else:
        print("You lose")