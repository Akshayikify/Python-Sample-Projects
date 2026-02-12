def start_game():
    name=input("Enter your name:")
    print(f"Welcome {name} for this adventure!")

    choice=input("You are stading in front of the cave .Specify whether you are going left or right: ").lower()
    if choice=="left":
        go_left()
    elif choice=="right":
        go_right()
    else:
        print("You have entered an invalid choice.")
        start_game()
def go_left():
    print("Okay , you have chosen to  go left")
    ans=input("Go left and find the river and take the gem.Decide whether you are gonna take or leave.").lower()
    if ans=="take":
        print("You have to take the gem from river and come back to the original position.")
        win_game()
    elif ans=="leave":
        print("Oh! You have to leave from this place , because you will be attacked and killed by a wampus")
        lose_game()
    else:
        print("You entered a wrong choice.You lost by thinking for long time.")
        lose_game()

def go_right():
    print("You have right.")
    ans=input("Go right and collect the wood from the forest and burn it in the fire. You burn or leave you decide.").lower()
    if ans=="burn":
        print("You burnt the wood in the fire and make the wampus run away from cave.")
        win_game()
    elif ans=="leave":
        print("Oh! you have this choice , you have to run fast and if you fail , you'll fall into the pit there.")
        lose_game()
    else:
        print("You have chosen an invalid choice , thus you lost.")
        lose_game()
def win_game():
    print("***Yeah! You won game!***")
def lose_game():
    print("***Oh! You lost this game , better luck next time***")
start_game()