#### CS 110 - Spring 2018
# Lab 5 - Experimenting With the 3n+1 Sequence
## Due Date: 5:00 p.m., February 22nd, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab5.py

### Grading Rubric

__Total: 15 Points__
* __Part A: 5 points__
    * seq3np1 function keeps track of and returns the count (3 points)
    * asks user for an upper bound for the range value (1 point)
    * uses the range (inclusively) (1 point)
* __Part B: 4 points__
    * Has a drawing function that takes the number of iterations as a parameter (3 points)
    * Graphs the results and updates world coordinates based on the largest value returned from seq3np1 (3 points)
    * Prints, on the graph, the max so far  (2 points)
* __Part D: 2 points__
    * Follows project structure, submission, and [formatting guidelines](https://docs.google.com/document/d/1RU9bHsJhc4wecOXelXF5uUjcNTce4f2I0-09kJKvRvk/) (1 point)
    * All functions have doc strings (see formatting guidelines for format) (1 point)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Refactor existing code
* Use a graph to gain more information about the 3n+1 sequence.
* Label a graph
________________


## Part A: 3n+1

In the lab5.py file, I have provided you with a 3n+1 function that currently prints the values in the sequence until it stops at 1. Remember that one of the interesting questions is “How many items are in the sequence before stopping at 1?” To determine this, we will need to count them.

Using the provided code, alter the function as follows:
* First, delete the print statements in the function
* Now we will need a local variable to keep track of the count.
    * It would make sense to call it `count`.
    * It will need to be initialized to 0 before we begin the loop.
* Once inside the loop, we will need to update count by 1 (increment), so that we can keep track of the number of iterations.
* When the loop terminates (we get to 1), return the value of `count`.

It is very important that you put these statements in the right place. Notice that the previous location of the print statements can be very helpful in determining the location.

This demonstrates an important pattern of computation called a counter (note that it is a type of accumulator). The variable count is initialized to 0 and then incremented each time the loop body is executed. When the loop exits, `count` contains the result — the total number of times the loop body was executed.

Since the function now returns a value, we will need to call the function inside of a print statement or save the result in a variable for later printing in order to see the result.

Now that we have a function that can return the number of iterations required to get to 1, we can use it to check a wide range of starting values. In fact, instead of just doing one value at a time, we can call the function iteratively in our `main`, each time passing in a new value. The algorithm for your main is as follows:
* Ask the user for a value to use for the upper bound of your range
* Create a for loop using an iteration variable called `start` that provides values from 1 up to (and __including__) the user supplied upper bound.
* Call the `seq3np1` function once for each value of `start`.
* Write a print statement that prints the value of `start` and the number of iterations.

__Show your TA your code, and that everything runs.__<br>
__--END OF IN LAB REQUIRED WORK. --__<br>
__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Graphing Data

### Keep track and graphing of the maximum number of iterations.
Next we will write a function that will take an upper bound value and use the turtle graphics library to graph the number of iterations, where the x axis is the upper bound and the y axis is the number of iterations. This provides an interesting visual that allows you to see the relative number of iterations for each value. You will need to:

* keep track of the maximum number of iterations
* use [setworldcoordinates](https://docs.python.org/3.6/library/turtle.html#turtle.setworldcoordinates) to make your graph re-scale according to the values you are graphing.
* Use a turtle to write out the loop variable and the number of iterations for the largest so far.

Scanning this list of results causes us to ask the following question: What is the longest sequence? The easiest way to compute this is to keep track of the largest count seen so far. Each time we generate a new count, we check to see if it is larger than what we think is the largest. If it is greater, we update our largest so far and go on to the next count. At the end of the process, the largest seen so far is the largest of all.

We can also use this value to update the y axis of the world coordinate. You can initialize your world coordinates to (0, 0, 10, 10), but then update them each time you get a new x value and new y value that is greater than the current max. You will need to update the graph on every iteration:
* positive x axis should be the current value of the loop iterator + 10
* the positive y axis should be the `max_so_far` value + 10
* The negative x and y values should both be 0

In other words, the world coordinates should grow with your graph. Below is the basic algorithm:
* Create a turtle and a window.
    * Create an additional turtle object to write out the maximum data
* Set the world coordinates to (0,0,10,10)
* Create a variable call `max_so_far` and initialize it to zero.
    * Place this initialization outside the for loop so that it only happens once.
* Write a for loop using the number of iterations passed as a parameter
* Now, inside the for loop, save the result of the `seq3np1` function in a variable called result.
* Then we can check result to see if it is greater than `max_so_far`.
    * If so, update `max_so_far`.
    * Using your writer turtle, clear the previous text if necessary
    * Add a label, “Maximum so far: <iteration>, <result>” using the turtles write method to write the iteration and result in the upper left corner of the screen (you can just use the max_so_far value as the y coordinate)
* Set the world coordinates of the screen to the current iteration and the `max_so_far` values.
* Graph the result with your turtle.

Experiment with different ranges of starting values.

## Part C: Submission
* Required code organization:
   * lab5.py

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
