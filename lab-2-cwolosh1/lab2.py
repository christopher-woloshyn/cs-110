import turtle              # 1.  import the modules
import random
import os

def main():
    window = turtle.Screen()       # 2.  Create a screen
    window.bgcolor('black')

    michelangelo = turtle.Turtle()    # 3.  Create two turtles
    leonardo = turtle.Turtle()
    michelangelo.color('orange')
    leonardo.color('blue')
    michelangelo.shape('turtle')
    leonardo.shape('turtle')


    michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
    leonardo.up()
    michelangelo.speed(0)
    leonardo.speed(0)    
    michelangelo.goto(-100,-160)
    leonardo.goto(-100,-180)


    # 5. your code goes here

    # Part A

    michelangelo_go = random.randrange(1,300)       # These are random movement values for the turtles.
    leonardo_go = random.randrange(1,300)         
                                   
    michelangelo.speed(1)                           # This slows the speed of the turtles so it's easier to see the race.
    leonardo.speed(1)
                                   
    michelangelo.forward(michelangelo_go)           # This implements each turtle's movement with the random values.
    leonardo.forward(leonardo_go)

    michelangelo.speed(0)                           # This increases the speed so the reset is more seemless.
    leonardo.speed(0)
                                   
    michelangelo.goto(-100,-160)                      # This resets the turtle's position to where it was.
    leonardo.goto(-100,-180)
    
    michelangelo_move1 = random.randrange(1,30)	    # These are the random movements of michelangelo
    michelangelo_move2 = random.randrange(1,30)
    michelangelo_move3 = random.randrange(1,30)
    michelangelo_move4 = random.randrange(1,30)
    michelangelo_move5 = random.randrange(1,30)
    michelangelo_move6 = random.randrange(1,30)
    michelangelo_move7 = random.randrange(1,30)
    michelangelo_move8 = random.randrange(1,30)
    michelangelo_move9 = random.randrange(1,30)
    michelangelo_move10 = random.randrange(1,30)

    leonardo_move1 = random.randrange(1,30)         # These are the random movements of leonardo
    leonardo_move2 = random.randrange(1,30)
    leonardo_move3 = random.randrange(1,30)
    leonardo_move4 = random.randrange(1,30)
    leonardo_move5 = random.randrange(1,30)
    leonardo_move6 = random.randrange(1,30)
    leonardo_move7 = random.randrange(1,30)
    leonardo_move8 = random.randrange(1,30)
    leonardo_move9 = random.randrange(1,30)
    leonardo_move10 = random.randrange(1,30)

    michelangelo.speed(1)                           # This slows the speed of the turtles so it's easier to see the race.
    leonardo.speed(1)

    michelangelo.forward(michelangelo_move1)        # This implements each turtle's movement with the earlier defined random values.
    leonardo.forward(leonardo_move1)

    michelangelo.forward(michelangelo_move2)
    leonardo.forward(leonardo_move2)

    michelangelo.forward(michelangelo_move3)
    leonardo.forward(leonardo_move3)

    michelangelo.forward(michelangelo_move4)
    leonardo.forward(leonardo_move4)

    michelangelo.forward(michelangelo_move5)
    leonardo.forward(leonardo_move5)

    michelangelo.forward(michelangelo_move6)
    leonardo.forward(leonardo_move6)

    michelangelo.forward(michelangelo_move7)
    leonardo.forward(leonardo_move7)

    michelangelo.forward(michelangelo_move8)
    leonardo.forward(leonardo_move8)

    michelangelo.forward(michelangelo_move9)
    leonardo.forward(leonardo_move9)

    michelangelo.forward(michelangelo_move10)
    leonardo.forward(leonardo_move10)

    michelangelo.speed(0)                           # This increases the speed so the reset is more seemless.
    leonardo.speed(0)
                                   
    michelangelo.goto(-100,-160)                    # This resets the turtle's position to where it was.
    leonardo.hideturtle()

    #Part B

    michelangelo.down()
    michelangelo.speed(2)
    michelangelo_side = 200

    michelangelo.forward(michelangelo_side)         # This is the triangle.
    michelangelo.left(120)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(120)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(120)
                      
    michelangelo.pencolor('red')

    michelangelo.forward(michelangelo_side)         # This is the square.
    michelangelo.left(90)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(90)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(90)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(90)

    michelangelo.pencolor('green')

    michelangelo.forward(michelangelo_side)         # This is the pentagon.
    michelangelo.left(72)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(72)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(72)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(72)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(72)

    michelangelo.pencolor('cyan')

    michelangelo.forward(michelangelo_side)         # This is the octogon.
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)
    michelangelo.forward(michelangelo_side)
    michelangelo.left(45)

    michelangelo.hideturtle()

    os.system('man man')
    os.system('man pwd')
    os.system('man mkdir')
    os.system('man rm')
    os.system('man cd')
    os.system('man ls')
    os.system('man mv')
    os.system('man cp')
    os.system('man python3')

    window.exitonclick()
main()
