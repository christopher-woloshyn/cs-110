#### CS 110 - Spring 2018
# Lab 4 - Making a Dartboard
## Due Date: 5:00 p.m., February 15th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab4.py

### Grading Rubric

__Total: 20 Points__
* __Part A: 7 points__
    * setupDartboard function works as expected (3 points)
    * throwDart function works as expected (4 points)
* __Part B: 8 points__
    * montiPi function works as expected (2 points)
    * isInCircle function works as expected (2 point)
    * drawSquare function works as expected (1 point)
    * drawLine function works as expected (1 points)
    * drawCircle function works as expected (2 points)
* __Part C: 3 points__
    * Uses an accumulator and loop to play the rounds (2 points)
    * Uses existing throwDart function (1 point)
* __Part D: 2 points__
    * Follows project structure, submission, and formatting guidelines (1 point)
    * All functions have doc strings (see formatting guidelines for format) (1 point)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Further break your code into reusable functions
* Use selection statements to conditionally execute code
* Run a Monte Carlo simulation
________________


## Part A: Approximating the Value of Pi


Almost everyone has heard of the famous mathematical constant called Pi. We use it most often to find the circumference or the area of a circle. For simplicity, the value that is commonly used for pi is 3.14. However, pi is an irrational number, meaning that that it has an infinite, non-repeating number of decimal digits. The value is
`3.1415926535897932384626433832795028841971693993751058209749445923078164062…`

In this lab, we will approximate the value of pi using a technique known as a Monte Carlo Simulation. This means that we will use random numbers to simulate a “game of chance”. The result of this game will be an approximation for pi.

### Setup

The game that we will use for this simulation is “darts”. We will “randomly” throw a number of darts at a specially configured dartboard. The set up for our board is shown below. In the figure, you can see that we have a round dartboard mounted on a square piece of wood. The dartboard has a radius of one unit. The piece of wood is exactly two units square so that the round board fits perfectly inside the square.

![](assets/dartboards.png?raw=true)

But how will this help us to approximate pi? Consider the area of the circular dartboard. It has a radius of one so its area is pi. The area of the square piece of wood is 4 (2 x 2). The ratio of the area of the circle to the area of the square is pi/4. If we throw a whole bunch of darts and let them randomly land on the square piece of wood, some will also land on the dartboard. The number of darts that land on the dartboard, divided by the number that we throw total, will be in the ratio described above (pi/4). Multiply by 4 and we have pi.

Using the provided driver code above, you will need to implement a function that sets up the dartboard as pictured above; however we are going to do this by breaking our setup into further functions. You should implement the following functions:
* `drawSquare(turtle, width, top_left_x, top_left_y)`
    * to outline dartboard
* `drawLine(turtle, x_start, y_start, x_end, y_end)`
    * to draw axes
* `drawCircle(turtle, radius)`
    * to draw the circle

Your `setUpDartboard()` function should be _almost_ entirely calls to the above three functions.

:bulb: You can write dummy functions or comment out the parts of the main() that you have not completed yet.

### Throwing Darts

Now that we have our dartboard setup, we can throw darts. We will assume that we are good enough at throwing darts that we always hit the wood (inside the window). Sometimes the darts will hit the dartboard and sometimes they will miss.
In order to simulate throwing the darts, we can use the [random](https://docs.python.org/3/library/random.html) module’s random() function generate two random floating point numbers between zero and one. The first will be the “x coordinate” of the dart and the second will be the “y coordinate”. However, we have a problem. The coordinates for the dartboard go from -1 to 1. How can we turn a random number between 0 to 1 into a random number between -1 and 1? What if we randomly (again) multiply by either -1 or 1?

#### Hints:
* In the first part, in order to turn the random number between 0 and 1 to a random number between -1 and 1, generate a random multiplier for each value using random.choice()
   * Read the documentation on this function so that you understand how to generate either -1 or 1 randomly
   * :bulb: random.uniform() works as well, and it accomplishes this in one line. Read the documentation on this function to learn how to use it.
* Then multiply each random multiplier by their associated random values to get your actual value for x or y

The driver (main) tests your code by “throwing” 10 darts at the dartboard in your main.

__Show your TA your code, and that everything runs.__<br>
__--END OF IN LAB REQUIRED WORK. --__<br>
__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Making the Plot Better
Once you understand what you have to do, using the provided driver code as a guide, complete the program, run and debug it as necessary.

:warning: You must use the provided template. Your code must implement the functions used in main as well as the functions described in the head comments

:bulb: Notice that only functions (or object methods) are called in the main. There is no program logic. This should be the structure of all procedural programs.

### Counting Darts
We already know the total number of darts being thrown. The variable `number_darts` keeps this for us. What we need to figure out is how many darts land in the circle? Since the circle is centered at (0,0) and it has a radius of 1, the question is simply a matter of checking to see whether the dart has landed within 1 unit of the center. Luckily, there is a turtle method called `distance` that will return the distance from the turtle to any other position. It needs the x,y for the other position.

For example, fred.distance(12,5) would return the distance from fred’s current position to position (12,5).

Now we need to use this method in a conditional to ask whether fred is within 1 unit from the center. You must meet the following requirements in your program:
* You should choose one color for darts that are within the circle, and a different color for darts outside of the circle.
* You must create a boolean function, `isInCircle(turtle)`, that returns `True` or `False` depending on if the turtle is within 1 unit away from the origin.  
* Create an accumulator variable, for example `insideCount`, initialize it to zero, and then increment it if we find that the dart is in the circle.
   * :bulb: Remember that the increment is a form of the accumulator pattern.

### The Value of Pi
After the loop has completed and visualization has been drawn, we still need to actually compute pi and print it. Use the relationship given above to get the ratio.

Run your program with larger values of `numdarts` to see if the approximation gets better.

* To summarize:
    * The Virtual Dartboard has an area of 2 X 2 (i.e., it  accommodates a unit circle)
        * Total area is 4
    * Since area of unit circle = pi * radius2 = pi (since radius squared = 1)
        * ratio of area of unit circle to area of board is pi/4
    * Theoretically, if you fill the entire board with darts, counting  the number of darts that fall within the circle divided by the total number of darts thrown should give us the same ratio (i.e., 1/4 * pi)
    * Therefore, multiplying this ratio by 4 should give us our approximation of pi
* See the attached file [lab5SampleOutput](https://drive.google.com/file/d/0B5NpY9dM1zfBTzZjOFhsY3AzT28/view?usp=sharing) for an 'in progress' example
     * :bulb: I made the world coordinates larger than the dartboard so I could see the ‘board’ better

## Part C: Game of Darts

Finally you will end your program by creating a function that plays a game of darts between two players. We will simplify the game of darts by saying that if the player lands inside the circle, she scores a point. There should be 10 rounds where the players take turns throwing darts. You should keep track of both players scores, then print which player has won or if there was a tie.
Your game function must:
* Use a loop to play the rounds
* Use an accumulator to keep track of players points
* Use your existing throwDart() function


## Part D: Submission
* Required code organization:
   * lab4.py

Below is just a reminder of the commands you should use to submit your code. If you cannot remember the exact process, please review Lab 1.

*These commands all presume that your current working directory is within the directory tracked by `git`.*

```git
git commit -a -m "first commit"
git push
```
Lastly we are going to make our final commit. You will need to do this when your submission is ready for grading.

```shell
git commit --allow-empty -m "final commit"
git push
```

:warning: Remember, you __MUST__ make a submission with the comment "final commit" before the deadline to be considered on time.
