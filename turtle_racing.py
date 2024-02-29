import turtle
import time
import random

WIDTH, HIGHT = 1300, 750
COLORS = ['black', 'red', 'orange', 'blue', 'pink', 'purple', 'brown', 'gray', 'yellow', 'cyan']


def get_number_of_turtles():        #Number of turtles
    turtles = 0
    while True:
        turtles = input("Enter the number of racers (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
            if 2 <= turtles <= 10:
                break
            else:
                print("Turtles must be 2 to 10")
        else:
            print("Amount must be an integer.")
            continue

    return turtles

def race(colors):       #Race script
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HIGHT // 2 -10:
                return colors[turtles.index(racer)]
            


def create_turtles(colors):     #Creating Turtles
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def init_turtle():      #Initializing Turtles
    screen = turtle.Screen()
    screen.setup(WIDTH, HIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)

print(f"{winner} is the winner of the race.")
time.sleep(5)