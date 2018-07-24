#### CS 110 - Spring 2018
# Lab 7 - Project Environment and L-Systems
## Due Date: 5:00 p.m., March 22th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* Driver Code
    * lab7.py
* Test Input Files
    * input1.txt
    * input2.txt
    * input3.txt

### Grading Rubric

__Total: 25 Points__
* __Part A: 5 points__
    * (3 pts) All team member have access to and have pulled from the final project repo
    * (2 pts) All team members have pygame installed on their own computer __or__ can run it on the lab machines with their project repo
* __Part B: 13 points__
    * applyRules() is placed in module and works correctly (4 points)
    * processString() is placed in module and works correctly (1 points)
    * createLSystem() is placed in module and works correctly (2 points)
    * drawLSystem() is placed in module and works correctly (4 points)
    * main function is only in the provided driver code file (2 points)
    * EXTRA CREDIT: Vary color and thickness in drawLSystem (2 points)
* __Part C: 6 points__
    * works with all sample input files (3 points)
    * Student supplied input file (3 points)
* __Part D: 1 point__
    * Follows project structure, submission, and formatting guidelines (1 point)
    * All functions (except main) have doc strings (see formatting guidelines for format) (1 point)


### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Setup your final project environment
* Use modules to make your code more modular
* Implement L-Systems
________________


## Part A: Beginning The Final Project

### Running Pygame
Pull the latest version of your final project github repo to the local machine. You may use the lab machines or your own laptop. Add the following lines of code to your `main.py`:

```python
import pygame

def main():
    pygame.init()
    #Create an instance on your controller object
main()
```

If you are running the code on your own laptop, you will need to install pygame. [Pygame](https://www.pygame.org/docs/) is a GUI library that we will be using for the final project. Once you learn how it works, it is  easy to use, but the initial learning curve can be steep.

Installing Pygame can be a difficult process, and is different for every machine, so you will have to figure this out on your own (google is your friend); however, here are some resources to help:

* https://www.pygame.org/wiki/GettingStarted
* https://jamesfriend.com.au/installing-pygame-python-3-mac-os-yosemite

:warning: Be sure you are installing pygame for _python3_, and __not__ _python 2_.

If you are using the lab machine, you can run python with pygame by using a specific version of python:

```shell
$ python3.2 main.py
```
:warning:Notice the `3.2`. This is the only version of python that can use pygame on the lab machines.

As long as everything runs without error, you are good to go on to the next part of the lab.

### Project Ideas

After you have completed the previous part of the lab, meet with me or a TA to discuss your project idea. Your team should have already agreed on a basic project idea and team roles, and your README should be updated accordingly. We will help you adjust the difficulty if needed, discuss next steps, and clarify team member duties.

__--END OF IN LAB REQUIRED WORK. --__

__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Modules and L-Systems

A module is a python source file that contains a set of functions and objects for you to use in your executable code. You can create a module by creating a file with your module functionality and importing it into your main script with:
```python
        import modulename  #drop the .py
```
For example, if you have a file called `musicplayer.py` that has a function that will play a music file, you could import and use it like so:
```python
        import musicplayer
        …
        musicplayer.play("discofever.mp3")
```
:warning: Keep in mind it must be in the same folder as the script that is using it.

Write the following L-System functions and place them in a module called `lsystems.py`:
* applyRules(char, rules)
   * Your applyRules function will take as parameters:
      * a single character
      * a set of rules as a dictionary
         * The format of the rules dictionary will be the following:
            * {'character1': 'substitution', 'character2':'substitution'}
         * For example, for the rules we had in class, you would receive a dictionary:
            * {'F':'F-F++F-F'}
            * {'A':'B', 'B':'AB'}
* processString(axiom, rules)
    * processes the entire string axiom by calliong apply rules on each character, and returns the new string
* createLSystem(iterations, axiom, rules)
    * runs the transformations on the axiom for a number of iterations as specified by iterations
* drawLSystem(orders, distance, degree)
    * draws the LSystem based on each character in the orders string, using the turtle library.
    * The symbols should correspond to the following actions:
        * F => forward(distance)
        * \+ => turn left by degree
        * \- => turn right by degree
        * [ => store state
        * ] => restore state

In the provided file, `lab7.py`, your lsystems module is imported, and  the driver code asks the user to input the following information:
* axiom
* number of iterations,
* angle
* distance
* number of rules

The main uses the number of rules to loop n times, and asks the user to input the rule in the specified format, `character:substitution`.

### Extra Credit

Instead of drawing with a single color and thickness, your turtle should vary color and line thickness randomly. It is up to you how often the color and thickness will vary, but it should be often enough to be discernable. For example:
* randomly change color and thickness every iteration
* change color whenever you turn right, and thickness when you turn left
* assign color based on direction and thickness based on distance from the origin

You can play around with this to see what you think produces the most interesting result.

## Part C: Testing your code

This program requires a lot of input from the user, so let’s look at how we can automate that part of testing. Even though your program will be written to retrieve input from from the user, which can correspond to the stream of input that the user types into the program, you need not interact directly with your program to be able to test it.

The unix `cat` command reads a file and prints it out to the screen. Try typing `cat lab7.py` from a command terminal prompt (not the python shell). You should see your python program, i.e. the contents of lab7.py. The shell pipe operator, `|` (a single vertical bar), connects the output of one program to the input of another. This means that you can type input meant for your program into a text file, which could be called `input1.txt`, for example. You could then `cat` the `input1.txt` file and pipe its output into your python program, exactly as follows:

```shell
cat input1.txt | python3 lab7.py
```

Your program should then behave exactly as if you typed the contents of `input1.txt` into the program, as prompted. Of course, this requires that `input1.txt` have the right kind of input, formatted appropriately, in the right order, etc. But once you get it set, you can include many commands and test the same sophisticated test cases over and over until they work, etc. Try it. The cover page has a link to 3 test files we will be using to test your code.

Once you know everything is working, create a fourth test file, `input4.txt`, with your own input values, following the same format as the previous input test files.

## Part D: Submission
* Required code organization:
   * lab7.py
   * lsystem.py
   * input1.txt
   * input2.txt
   * input3.txt
   * input4.txt

Below is just a reminder of the commands you should use to submit your code. If you cannot remember the exact process, please review Lab 1.

*These commands all presume that your current working directory is within the directory tracked by `git` and all necessary files have been added to the repo.*

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
