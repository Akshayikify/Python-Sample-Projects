#The new project-dice-roll using random module
import random 
random_num=random.randint(1,6)
user_input=input("Are you interested in playing dice roll game?(y/n)  ").lower()
if user_input=='y':
    print("Welcome to dice rolling game.")
    dice_roll=random_num
    print(f'The rolled dice number is {dice_roll}')
else:
    print("oh! Try next time.")
print("Thanks for playing game.")