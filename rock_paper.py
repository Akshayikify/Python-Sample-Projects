import random

user_win=0
computer_win=0

choices=["rock","paper","scissors"]
while True:
    user_input=input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in choices:
        continue
    random_num=random.randint(0,2)
    computer_guess=choices[random_num]
    print("The computer Pick:",computer_guess)
    
    if user_input=="rock" and computer_guess=="scissors":
        print("You won!")
        user_win+=1
    elif user_input=="paper" and computer_guess=="rock":
        print("You won!")
        user_win+=1
    elif user_input=="scissor" and computer_guess=="paper":
        print("You won!")
        user_win+=1
    else:
        print("Computer won!")
        computer_win+=1
print(f"You won {user_win} times.")
print(f"Computer won {computer_win} times.")
print("Game Ends. Happy Gaming.")