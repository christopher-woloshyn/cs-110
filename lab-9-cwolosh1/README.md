#### CS 110 - Spring 2018
# Lab 9 - Working with Pygame
## Due Date: 5:00 p.m., April 19th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Provided Code and Test Files
* Provided Code
    * lab9.py
    * hero.py
    * enemy.py

### Grading Rubric
__Total: 20 Points__
* __Part A: 5 points__
    * Enemies randomly move around the screen
        * Only the update method should change for Part A.
* __Part B: 13 points__
    * Unique additional feature added
    * EXTRA CREDIT: Best of section (5 points)
* __Part C: 2 points__
    * Follows project structure, submission, and formatting guidelines (1 point)
    * All functions (except main) have doc strings (see formatting guidelines for format) (1 point)


### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Understand basic GUI structure
* Use pygame to add features to an existing program

***

## Part A: Understanding Pygame

Within this lab I have provided you with a very simple game using the pygame library. As it stands it is not very robust and doesn't have any features. The first thing you should do is run the code and make sure you understand how all parts of it work. Notice the file structure and how the source code is separated from the image files. Next, review the code itself. Look at the pygame [documentation](https://www.pygame.org/docs/ref/sprite.html) to try to understand what all the code is doing.

:bulb: Remember, you have to use `python3.3` to run pygame in the linux lab. If you have any questions, ask the CA's for clarification.

### Adding a Feature

Once you feel like you understand what is happening, we are going to make the enemies to randomly move around the screen. Each enemy is part of a sprite group that has an update method which calls the individual update method for each member of the group on each iteration through the mainloop. Currently, this method just prints out "update me" to the console. What you need to do is alter the update method for the enemy class so that it changes both the x and y coordinate of the internal rectangle object by -1, 0, or 1.

You do not have to implement the following, but you should think about how you would accomplish these:
* Can you keep the enemies from going off screen?
* How would you have them move towards the hero?

__Show your TA your code. If you were not able to finish, show the TA what you have completed.__

__--END OF IN LAB REQUIRED WORK--__

__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Adding a Feature

Now is your moment to shine. For part B you are going to add your own additional feature to the game, just like we did in part A. It can be anything you like, but should be a unique additional feature of your own choosing. In other words, you must add to the game, not just modify it. For example:
* :no_entry_sign: Change the hero health from 3 to 5
* :heavy_check_mark: Make the enemies to randomly move

You may use anything from the pygame library and any resources (images, media) you like. You must keep the provided file structure. If you are unsure whether or not the additional feature is okay, ask your CA.

***
### __UNIQUE FEATURE DESCRIPTION__

Added a health feature to the GUI. The hero now has "max health" and "current health" attributes. The current health is displayed in the top right corner of the screen; one heart represents one health. The function is built such that any future change in the hero's max health will still fit the hearts on the screen. For example, the hero has 3 health and 3 hearts appear in the top right corner, but if the hero's max health were to be changed to 5, the function will automatically fit 5 hearts on the screen in the same position on the corner, accomodating for more future changes.

***
### Extra Credit (5 points)

The best new feature from your section will receive extra credit. Each CA will choose one person from their section as a feature winner. I will choose the best out of the 5 winners to incorporate into the code base for future labs (with appropriate credit given, of course).

:warning: Only add 1 new feature. If you add more than one, your submission will not be eligible for extra credit.

## Part C: Submission
* Required code organization:
    * lab9.py
    * src
        * hero.py
        * enemy.py
    * assets
        * hero.png
        * enemy.png

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
