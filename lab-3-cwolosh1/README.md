#### CS 110 - Spring 2018
# Lab 3 - Turtle Racing Lab
## Due Date: 5:00 p.m., February 1st, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* N/A

### Grading Rubric

**_TOTAL: 15 points_**
* **Part A: 7 points**
   * Creates a function for drawing the sine function and calls the function from main (3 points)
   * Draw sine function using a loop (4 points)
* **Part B: 7 points**
   * Setup window function set world coordinates to requested values (2 points)
   * Setup turtle function draws the x and y axis with the origin at the center (2 points)
   * Draws from -360 to 360 on the x axis (1 point)
   * Draw cosine function (2 points)
* **Part C: 1 point**
    * Follows requested project structure and submission format
    * Follows [formatting guidelines](https://docs.google.com/document/d/1RU9bHsJhc4wecOXelXF5uUjcNTce4f2I0-09kJKvRvk/edit?usp=sharing)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:

* Use the turtle library to graph equations
* Write a function

| | Meaning |
|:----:|---------|
| :bulb: | Tips and useful information |
| :warning: | Caution! This could cause you problems. |
| :no_entry_sign: | Danger! Don't do this! |

## Part A: Drawing

Have you ever used a graphing calculator? You can enter an equation, push a few buttons, and the calculator will draw a line. In this exercise, we will use our turtle to plot a simple math function, the sine wave.

### What is the sine function?
The sine function, sometimes called the sine wave, is a smooth, repetitive oscillation that occurs often in many fields including mathematics, physics, and engineering. A single repetition is shown below. Note that the x axis is given in degrees.

![](assets/sinpic.png?raw=true)

For this lab, we will use the math library to generate the values that we need. To help you understand the sine function, consider the following Python program.
```python
import math
def main():
	y = math.sin(math.radians(90))
    print(y)
main()
```
As you can see, the `sin` function from the math library takes a single parameter. This parameter must be a value in “radians” (you may remember this from trigonometry class). Since most of us are used to stating the size of an angle in “degrees”, the math module provides a function, `radians` that will convert from degrees to radians for us.
Now try it for some other boundary values, like 270 or 360.

### Making the Plot

In order to plot a smooth line, we will use the turtle’s [`goto`](https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.goto) method. `goto` takes two parameters, __x__ and __y__, and moves the turtle to that location. If the tail is down, a line will be drawn from the previous location to the new location.

```python
import math
import turtle

def main():
    wn = turtle.Screen()
    fred = turtle.Turtle()
    fred.goto(50,60)
    wn.exitonclick()
main()
```
Recall that the default turtle screen starts with the turtle in the middle at position (0,0). You can think of the screen as a piece of graph paper. The x axis runs horizontally and the y axis runs vertically. The point where they meet in the middle is (0,0). Positions to the left of the center have an x value that is negative. Positions that are below the center have a y value that is negative.

![](assets/graphpaper.jpg?raw=true)

Let’s try the `goto` method. Experiment with the method to make sure you understand the coordinate system of the screen. Try it yourself by choosing random numbers for your `goto`. Test all combinations (4) of positive and negative x and y coordinates.

Now we can put the two previous programs together to complete our plot. Write a complete program that does the following:
* Create and set up the turtle and the screen.
* Write a function that uses a loop to draw a sine curve by iterating the angle from 0 to 360.
    * Generate the sine value for each angle.
    * Move the turtle to that position (leave a line behind).
* Call your function from your main()

__:warning: This will not produce the expected result. That is intentional.__

__Show your TA your code.__

__--END OF IN LAB REQUIRED WORK--__

_You may continue to work on the remainder of the lab on your own time or in lab_

## Part B: Making the Plot Better
You probably think that the program has errors since it does not draw the picture we expect. Maybe you think it looks a bit like a line? What do you think the problem is? Here is a hint...go back and take a look at the values for the sine function as they were calculated and printed in the earlier example.

Now can you see the problem? The value of sin always stays between -1 and 1. This does not give our turtle much room to run. In order to fix this problem, we need to redesign our “graph paper” so that the coordinates give us more room to plot the values of the sine function. To do this, we will use a method of the `Screen` class called `setworldcoordinates`. This method allows us to change the range of values on the x and y coordinate system for our turtle. Take a look at the documentation for the turtle module to see how to use this method (Global Module Index). Once you have an understanding of the parameters required to use the method, choose an appropriate coordinate system and retry your solution.

* :bulb: There are a couple of tricky parts here:
    * You must draw the curve from -360 degrees all the way back to 360 degrees (inclusive)
    * The `math.sin()` function only takes degrees in radians
        * It may be useful to place a print() debug statement after determining x and y so that you can see if their values are reasonable
        * Question:  What is 360 degrees in radians?
    * In order to scale the window properly (setworldcoordinates()) you need to determine the lowest and highest x values as well as the lowest and highest y values
* Improve upon the solution in the textbook by using functions:
    * In the main() method, create the Screen and the Turtle, and invoke functions to set up the window, set up the Turtle, and draw the sine curve
    * Create the following functions:
        * `setUpWindow(screenObject)`
            * to set coordinates and background color
        * `setUpTurtle(turtleObject)`
            * to draw the x and y axis with the origin (0, 0) at the center of the screen and place a turtle object in the correct place to start drawing curve
    * :warning: Make sure the type of the argument sent to each function matches the type and order of the function parameter(s)

__Now try this...__

Now that you can plot a sine function, how about trying a different function, such as cosine? Create an additional function called `drawCosineCurve()`.

Make sure you test both curve functions in your driver (main function).

## Part C : Code Organization and Submission
* Required code organization:
   * lab3.py

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
