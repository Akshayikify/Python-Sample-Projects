import random
guesses=0
while True:
    guesses+=1
    try:
        num=int(input("Type a number:"))
        if num<=0:
            print("Please enter the number greater than 0 next time.")
            quit()
        random_num=random.randint(1,10)
        if num==random_num:
            print("Yeah! you guessed right!")
            break
        elif num<random_num:
            print("Too low")
        else:
            print("Too high")
    except Exception:
        print("Please a number.")
print(f"You got it with {guesses} guesses.")
 