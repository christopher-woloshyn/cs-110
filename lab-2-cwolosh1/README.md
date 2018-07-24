#### CS 110 - Spring 2018
# Lab 2 - Turtle Racing Lab
## Due Date: 5:00 p.m., February 1st, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* N/A

### Grading Rubric

**_TOTAL: 15 points_**
* **Part A: 4 points**
   * Race 1 consists of a single call for each turtle (1 point)
   * Race 2 uses random values for advancing (1 point)
   * Turtle positions are reset after each race (2 points)
* **Part B: 10 points**
   * Turtle correctly draws a triangle, square, pentagon, and octagon (4 points)
   * imports os module and calls man pages for all requested commands (4 points)
   * Enclosed in a main. Only the call to main and imports are in global space. (2 points)
* **Part C: 1 point**
    * Follows requested project structure and submission format
    * Follows [formatting guidelines](https://docs.google.com/document/d/1RU9bHsJhc4wecOXelXF5uUjcNTce4f2I0-09kJKvRvk/edit?usp=sharing)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:

* Import modules from the python library
* Generate random values
* Use the turtle library to draw images

| | Meaning |
|:----:|---------|
| :bulb: | Tips and useful information |
| :warning: | Caution! This could cause you problems. |
| :no_entry_sign: | Danger! Don't do this! |

## Part A: Random Numbers

Before we begin writing code for this lab, we need to introduce one more Python module.
The random module allows us to generate random numbers. It’s easy to use:
```python
import random
def main():
    x = random.randrange(1,10)
    print(x)
main()
```
The randrange function as called in the example above, generates a random number from 1 to 9.
Even though we said 10 the randrange function goes up to, but does not include
the upper limit value. Now if you run the program over and over again you should
 see that each time you run it a different number is generated. Random numbers
 are the basis of all kinds of interesting programs we can write, and the
 randrange function is just one of many functions available in the random module.

### Turtle Races
In this lab we are going to work step by step through the problem of racing turtles. The idea is that we want to create two or more turtles and have them race across the screen from left to right. The turtle that goes the farthest is the winner.
There are several different, and equally plausible, solutions to this problem. Let’s look at what needs to be done, and then look at some of the options for the solution.

To start, let’s think about a solution to the simplest form of the problem, a race between two turtles. We’ll look at more complex races later. When you are faced with a problem like this in computer science it is often a good idea to find a solution to a simple problem first and then figure out how to make the solution more general.
Here is a possible sequence of steps that we will need to accomplish:
1. Import the modules we need
2. Create a screen
3. Create two turtles
4. Move the turtles to their starting positions
5. Send them moving across the screen
Here is the Python code for the first 4 steps above. I have created a file for you in the repo that has this code already written.
```python
import turtle              # 1.  import the modules
import random


def main():
    window = turtle.Screen()       # 2.  Create a screen
    window.bgcolor('lightblue')


    michelangelo = turtle.Turtle()    # 3.  Create two turtles
    leonardo = turtle.Turtle()
    michelangelo.color('orange')
    leonardo.color('blue')
    michelangelo.shape('turtle')
    leonardo.shape('turtle')


    michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
    leonardo.up()
    michelangelo.goto(-100,20)
    leonardo.goto(-100,-20)

    # 5. your code goes here



    window.exitonclick()
main()
```
:bulb: You can review the documentation for the turtle library, with its list of methods, [here](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)

Now, you have a couple possibilities for how to fill in code for step 5. Try coding each of the following to see the different kinds of behavior.
1. Use a single call to forward for each turtle, using a random number between 1-300 as the distance to move.
   * Reset the turtles to their starting position [(-100, 20), (-100, -20) respectively] once you are done.
2. Make 10 calls to forward alternating on each turtle with the random range between 0 and 30.
   * The random value should be generated again for each call to forward.
   * Reset the turtles to their respective starting positions once you are done.

So, which of these programs is better? Which of these programs is most correct? These are excellent questions. Method 1 is certainly the simplest, but it isn’t very satisfying as far as a race is concerned. Each turtle simply moves their distance on their turn. Method 2 is probably the most ‘realistic’ assuming realism is very important when we’re talking about a simulated race of virtual turtles, but we are writing a lot of repeated code. We’ll look at how to solve this problem next week.

You may be thinking, “why can’t each turtle just move forward until they cross some artificial finish line?” In other words, move until some condition is met rather than moving a set number of times. Good question! We’ll get to the answer in a later lesson when we learn about something called the while loop.

__Show your TA your code.__

__--END OF IN LAB REQUIRED WORK--__

_You may continue to work on the remainder of the lab on your own time or in lab_

## Part B: Modules
Write additional code in your main to have your turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
* An equilateral triangle
* A square
* A pentagon (5 sides)
* An octagon (8 sides)

You can also import the Operating System as a module in your code. Add the following to the top of your script:
```python
import os
```
You can now run terminal commands from within Python with the command:
```python
    os.system(“<command>”)
```
For example, if I wanted to print out the folder contents, I could call: 
```python
    os.system(“ls”).
```
Write code to print out the man page for each of the commands you looked up in lab 1:
* man
* pwd
* mkdir
* rm
* cd
* ls
* mv
* cp
* python3

:warning: When you run the code for testing, you will have to type ‘q’ after each command to move onto the next one

:warning: If you get ‘no manual entry’ for some of the commands, that’s okay

:no_entry_sign: These commands will not work on a Windows machine

## Part C : Code Organization and Submission
* Required code organization:
   * lab2.py

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
