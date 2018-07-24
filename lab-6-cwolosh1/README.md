#### CS 110 - Spring 2018
# Lab 6 - Working with Strings
## Due Date: 5:00 p.m., March 1st, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab6.py
   * _You must use this driver code without alteration other than completing the functions_
### Grading Rubric

__Total: 15 Points__
* __Part A: 12 points__
   * (4 pts) donuts() passes all tests
   * (4 pts) both_ends() passes all tests
   * (4 pts) fix_start(s) passes all tests
* __Extra Credit:__
   * (3 pts) Complete each function with a single line of code. No partial credit.
* __Part B: 3 points__
   * Follows project structure, submission, and formatting guidelines (1 point)
   * All functions have doc strings (see formatting guidelines for format) (1 point)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Work with strings
* Start on your Final Project
________________


## Part A: Working with Strings

Over the next few weeks we will begin working with data structures. One of the simplest data structures that you have already seen is strings. While you have been working with strings already, you may not know what they do or what they really are. To start thinking about strings as a data structure, we have to understand what as string really is.

Since computers don’t understand words, we have to build up strings out of characters. So essentially, a string is a list of characters in order. A string can be any length, including 0. An empty string is just a string that has 0 characters. In Python, strings are immutable, meaning you cannot alter them after they have been defined. Once you create a string, “Hello”, that string can never change.

However, you can manipulate existing strings to create new ones. There are three main python features that you will need to use to complete this lab.
1. Since strings are just lists of characters, we can index into strings to access specific letters, just like we would index into a list.
   * For example, if I had
    ```python
    mystring = "Hello"
    ```
    I could access the first character with `mystring[0]`. The index of the first character is always 0, not 1.
    ```python
        print(mystring[0]) #prints 'H'
    ```
2. We can also index from the end of the string (instead of the beginning) by using negative numbers for an index. So I could access the last character with `mystring[-1]`
    ```python
    print(mystring[-1]) #prints ‘o’
    ```
3. You can get the length of a string using the len() function by passing the string as an argument
   ```python
   mystring = 'Hello'
   size = len(mystring) #returns 5
   ```
4. Lastly, you can concatenate two or more strings with the + symbol.
      ```python
      mystring = "Hello" + "" Goodbye"
      print(mystring) #prints “Hello Goodbye”
      ```

I have provided you with driver code above containing 3 functions I would like you to complete.
* `def donuts(count)`:
    * Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count. So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
* `def both_ends(s)`:
    * Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead an empty string.
* `def fix_start(s)`:
    * Given a string s, return a string where all occurrences of its first char have been changed to '*', except do not change the first char itself. e.g. 'babble' yields 'ba**le'. Assume that the string is length 1 or more.

Using the above features of strings, complete the 3 functions in the driver code given to you. You are also welcome to use any additional string functions or features available in python.

__Show your TA your code, and that everything runs.__

__--END OF IN LAB REQUIRED WORK. --__

__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Final Project Introduction

Each of you will work with two other individuals from the class to develop and implement the project. The project description is found [here](https://docs.google.com/document/d/1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE/edit?usp=sharing).

:warning: _You may not work on the project alone. This project is more about working on a software development team than it is about the final result._

You should start your project by:
1. Deciding on your team, and team roles.
2. Decide on a team name. You cannot change this, but it doesn't have to relate to your project.
3. The __Software Lead__ should accept the assignment link to the [repo](https://classroom.github.com/g/gtvmlaQZ) on Github, and enter the team name.
4. The rest of the the team should then accept the [assignment link](https://classroom.github.com/g/gtvmlaQZ) and select the appropriate team.
5. Update the README for your project with your project idea, along with every other section
    * Remember, most of this will be TBD, and nothing is set in stone

By next Friday's lab (_March 2nd_) you should have a rough idea of what you want to do for your project. Don't worry about the difficulty, we will help you scale it appropriately to what you can actually do.

:warning: This is your first grade for the final project. Getting your repo set up, everybody having access to it, and your README updated is the first 5% of your final project grade.

:bulb: In general, it is better to shoot for the stars, then we can scale it back if necessary.

## Part C: Submission
* Required code organization:
   * lab6.py

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
