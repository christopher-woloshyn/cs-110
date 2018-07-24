#### CS 110 - Spring 2018
# Lab 10 - Working with Pygame
## Due Date: 5:00 p.m., April 26th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Provided Code and Test Files
* Provided Code
    * lab10.py
    * hilbertcurve.txt
    * dragoncurve.txt
    * arrowheadcurve.txt
    * peanogospercurve.txt
    * sierpinskitrianglecurve.txt

### Grading Rubric
__Total: 20 Points__
* __Part A: 18 points__
    * Contains a L-System Class in a seperate file, `lsystems.py` (2 points)
    * L-System class separates string generation and visualization (3 points)
    * HilbertCurve (2 points)
    * DragonCurve (2 points)
    * ArrowheadCurve (2 points)
    * PeanoGosperCurve (2 points)
    * SierpinskiTriangleCurve (2 points)
    * Exception handling (3 points)
* __Part C: 2 points__
    * Follows project structure, submission, and formatting guidelines (1 point)
    * All functions (except main) have doc strings (see formatting guidelines for format) (1 point)


### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Read Files
* Work with Exceptions

***

## Part A: Understanding Pygame

We’ve already completed several labs with L-Systems. In this lab we will expand our L-System to a more robust MVC architecture. We are going use the following components:
* Model
   * LSystem class that reads from a file _(you will write this)_
* View
   * The Turtle Library
* Controller
   * main function that initializes a loop that will display each file _(provided for you)_

There are some standard L-System patterns, such as the serpinski triangle, that you can generate using L-Systems. I have placed the L-System data for common patterns into a file for your program to read in. You will write the class that reads in a set of rules from a file, and implements those rules in your code. The file format will be as follows:
```
        angle
        iteration
        axiom
        symbol : substitution
        ...
```
An unknown number of substitutions may follow the axiom, i.e. the specific LSystem may have more than 2 rules, so you must design accordingly. For example, the hilbertcurve.txt file will have:
```
        90
        4
        L
        L : +RF-LFL-FR+
        R : -LF+RFR+FL-
```
You may assume well-formed files and don’t need to worry about error checking the format.

* hilbertcurve.txt
* dragoncurve.txt
* arrowheadcurve.txt
* peanogospercurve.txt
* sierpinskitrianglecurve.txt

Create an L-System class that that takes a filename, and reads in a set of symbols and rules. The filename should be passed to the __init__ method, which reads in the rules, angle, and iterations, then stores them all. I recommend storing the rules in a dictionary, but implementation is up to you. Below is a __pseudocode__ example of the algorithm in the init method:

```python
file = open_file
angle = file.readline
iterations = file.readline
axiom = file.readline
for line in file:
        rules += [line]
```

Your class must have the interface used in the provided driver code. You must have exception handling in your class in case the file does not exist. Since you are reading in the file in your init, your exception handling should go there. The program should not break on an invalid filename, so you must have some sort of fallback.

For some interesting reading on similar patterns see:  
* http://fractalfoundation.org/resources/what-are-fractals/
* http://www.wired.com/2011/02/turing-patterns/#slideid-591130
* http://www.wired.com/2011/02/turing-patterns/#slideid-591127
* http://en.wikipedia.org/wiki/Rule_30

__Show your TA your code. If you were not able to finish, show the TA what you have completed.__

__--END OF IN LAB REQUIRED WORK--__

__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: ATP

Complete your ATP for your final project. You will put together an Acceptance Test Procedure (ATP) that shows your program working. Note the example one provided here and in the sample proposal.
* The ATP must:
    * be thorough and efficient
    * show how ALL of your program features work and that they work correctly
    * include steps that deal with how the program prevents or handles user error
* Note how the [sample ATP](https://docs.google.com/document/d/1-mKaTZHVGFH7TqWnAozR-NY0v6SXPdxceX74gE-KYNM/edit?usp=sharing) in the project description illustrates all of the features of the GUICounter program, and how each step is arranged to set up the next test efficiently without undue repetition. You MUST write your ATP in the same tabular fashion illustrated in the sample provided.
    * :bulb: You may write this as a google doc and link it in your Proposal if you feel that is easier than writing it in markdown.

Columns must be the same as shown:  
* Step: step number
* Procedure:  exact procedure for tester to follow
* Expected Results:  description of results to be expected - must be EXACT
    * Examples:
        * Procedure:  Enter a value into the entry box
        * Expected Results:  value is displayed:  Incorrect, not exact
        * Procedure:  Go to Set Counter entry box, enter 10 and press <Enter>  |  
        * Expected Results:  Display changes to Count = 10:  Correct, exact procedure and exact result
* Actual Results:  LEAVE BLANK - will be filled in with appearance of results that actually occur during your demo
* Pass: LEAVE BLANK
Notice you will have completed this before you complete your final project. This gives you a list of items that are must haves (i.e. you must get working).

## Part C: Submission
* Required code organization:
    * lab10.py
    * lsystem.py
    * hilbertcurve.txt
    * dragoncurve.txt
    * arrowheadcurve.txt
    * peanogospercurve.txt
    * sierpinskitrianglecurve.txt

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
