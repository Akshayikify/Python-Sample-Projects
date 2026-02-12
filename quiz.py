print("Hey! Welcome to quiz game!")
name=input("Enter your name:")
playing=input("Do you want to play(y/n)? ").casefold()
if playing !="yes":
    quit()

print("Okay! Let's play!->")

score=0
answer=input("What does CPU stands for? ").casefold()
if answer=="Central Processing Unit".casefold():
    score=score+1
    print(f"Yeah! You won!")
else:
    print(f"Oh! You lose")
    
answer=input("What does GPU Stands for? ").casefold()
if answer=="Graphic Processing Unit".casefold():
    score=score+1
    print(f"Yeah! You won!")
else:
    print(f"Oh! You lose")
    
answer=input("What does RAM stands for? ").casefold()
if answer=="Random Access Memory".casefold():
    score=score+1
    print(f"Yeah! You won!")
else:
    print(f"Oh! You lose")

answer=input("What does ROM stands for? ").casefold()
if answer=="Read Only Memory".casefold():
    score=score+1
    print(f"Yeah! You won!")
else:
    print(f"Oh! You lose")

print(f"Hurray! {name} your score is {score}")
print(f"Hurray! {name} you are  {score*100//4}% Correct")