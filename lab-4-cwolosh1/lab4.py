'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(turtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(turtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(turtle, radius) - to draw the circle
  setUpDartboard(screen, turtle) - to set up the board using the above functions
  isInCircle(turtle, circle_center, radius) - determine if dot is in circle
  throwDart(turtle)
  playDarts(turtle)
  montePi(turtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

# List constants here (NO MAGIC NUMBERS!):
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
RIGHT_ANGLE = 90

#########################################################
#                   Your Code Goes Below                #
#########################################################

def drawSquare(tortle, width, top_left_x, top_left_y):
    """ Draws a square with a turtle at a specified location.

        args: tortle [turtle.Turtle] - the object used to draw the square
              width[int] - the length value of each side of the square
              top_left_x [int] - the x coordinate of the top left corner of the square
              top_left_y [int] - the y coordinate of the top left corner of the square

        return: none
    """
    tortle.up()
    tortle.goto(top_left_x,top_left_y)
    tortle.down()
    for i in range(4):
        tortle.forward(width)
        tortle.right(RIGHT_ANGLE)
        
def drawLine(tortle, x_start, y_start, x_end, y_end):
    """ Draws a line with a turtle between two points.

        args: tortle [turtle.Turtle] - the object used to draw the line
              x_start [int] - the x coordinate for the starting point of the line
              y_start [int] - the y coordinate for the starting point of the line
              x_end [int] - the x coordinate for the ending point of the line
              y_end [int] - the y coordinate for the ending point of the line

        return: none
    """
    tortle.up()
    tortle.goto(x_start, y_start)
    tortle.down()
    tortle.goto(x_end, y_end)
    
def drawCircle(tortle, radius):
    """ Draws a circle of a certain radius with a turtle.

        args: tortle [turtle.Turtle] - the object used to draw the circle
              radius [int] - the radius of the circle that is drawn

        return: none              
    """
    tortle.penup()
    tortle.goto(0,-1)
    tortle.pendown()
    tortle.circle(radius, steps=360)
    
def setUpDartboard(screen, tortle):
    """ Uses previously defined functions to draw an x-y axis, draw a square, and draw an inscribed circle.

        args: screen [turtle.Screen] - inputs the screen so the world coordinates can be changed
              tortle [turtle.Turtle] - the object used to draw the aforementioned shapes

        return: none
    """
    tortle.reset()
    screen.setworldcoordinates(-2, -2, 2, 2)
    drawSquare(tortle, BOARD_WIDTH, -1, 1)
    drawLine(tortle, -2, 0, 2, 0)
    drawLine(tortle, 0, -2, 0, 2)
    drawCircle(tortle, 1)

def throwDart(tortle):
    """ Moves a turtle to a random point within the drawn square, and marks where the dart hits the target. If it lands within the circle, the dart's mark will be blue, if it lands outside the circle, the dart's mark will be red.

        args: tortle [turtle.Turtle] - the object used to mark where the "dart" hits the target

        return: none
    """
    num_x = random.random()
    num_y = random.random()
    neg = [-1, 1]
    neg_int_x = random.choice(neg)
    neg_int_y = random.choice(neg)
    x = num_x * neg_int_x
    y = num_y * neg_int_y

    tortle.penup()
    tortle.goto(x, y)
    if isInCircle(tortle, (0,0), 1):
        tortle.color('blue')
        tortle.dot()
        tortle.color('black')
    else:
        tortle.color('red')
        tortle.dot()
        tortle.color('black')

def isInCircle(tortle, circle_center, radius):
    """ Checks if a turtle is in the circle by comparing its distance from the circle's center to the radius of the circle.

        args: tortle [turtle.Turtle] - the object who's distance is compared to the radius of the circle
              circle_center [tuple] - the coordinate point representing the center of the circle
              radius [int] - the value that is compared to the distance between the turtle an the circle's center, to determine if that point is in the circle

       return: a boolean.
    """
    return tortle.distance(circle_center) < radius

def montePi(tortle, num_darts):
    """ Estimates the value of pi by taking the ratio between a number of darts thrown at the target that land in the circle, with the total number of darts thrown, and then multiplying that number by 4.

        args: tortle [turtle.Turtle] - the object used to mark where the dart hits the target.
              num_darts[int] - the total number of darts to be thrown at the target

        return: an approximation of pi.
    """
    inside_count = 0
    for i in range(num_darts):
        throwDart(tortle)
        if isInCircle(tortle, (0,0), 1):
            inside_count += 1
    return((float(inside_count) / float(num_darts)) * 4) #function returned 0 after dividing integers so I converted both to float.

def playDarts(tortle):
    """ Plays a simulated game of darts by having two players switch off throwing a dart for ten rounds. Each player's score will increase by one if their dart is in the circle. At the end of each round the current score will be printed. The player with the highest score at the end of the 10 rounds will be the winner!

        args: tortle [turtle.Turtle] - the object used to mark where the "dart" hits the target.

        return: The current score between the players each round. The winner after 10 rounds.
    """
    player1_score = 0
    player2_score = 0
    for i in range(10):
        throwDart(tortle)
        if isInCircle(tortle, (0,0), 1):
            player1_score += 1
        throwDart(tortle)
        if isInCircle(tortle, (0,0), 1):
            player2_score += 1
        print('Player 1 has ' + str(player1_score) + ' point(s). Player 2 has '+ str(player2_score) + ' point(s).')
    if player1_score > player2_score:
        print("Player 1 is the winner!")
    elif player2_score > player1_score:
        print("Player 2 is the winner!")
    else:
        print("Neither player has one; it's a draw!")

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)

    print("\tPart A Complete...")
    print("=========== Part B ===========")
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear() # CHANGED "window.clear()" TO "darty.clear()" AS MENTIONED IN CLASS!
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
