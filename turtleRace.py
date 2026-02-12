import turtle
import time
import random

#Specifying the height & width of turtle screen
HEIGHT,WIDTH=500,500
COLORS=['red','orange','green','cyan','blue','pink','brown','purple','yellow','black']

def get_num_of_racers():
    racers=0
    while True:
        racers=input("Enter the number of turtles (2-10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Enter the number only.")
            continue
        if racers>=2 and racers<=10:
            return racers
        else:
            print("Enter the valid number.")

def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)
            
            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]
def create_turtles(colors):
    turtles=[]
    spacex=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.shape('turtle')
        racer.speed(1)
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacex,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    #Creting the screen 
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!')
racers=get_num_of_racers()
init_turtle()

random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print(f"The winning turtle is with color  {winner}")
time.sleep(5)


