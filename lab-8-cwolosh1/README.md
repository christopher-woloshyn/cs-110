#### CS 110 - Spring 2018
# Lab 8 - Defining your Models
## Due Date: 5:00 p.m., March 29th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* Driver Code
    * lab8.py

### Grading Rubric
__Total: 20 Points__
* __Part A: 13 points__
    * Rectangle class has x, y, width, height instance variables [2 points]
    * Rectangle class has __init__ that properly sets all instance variables [2 points]
    * Rectangle class has __str__ that returns a string and does not print [3 points]
    * Surface class has rectangle and image instance variables [2 points]
    * Surface class has __init__ that properly creates Rectangle object and sets instance variable
* __Part B: 5 points__
    * Proposal Document updated to reflect model structure [2 points]
    * Tests for each method of each proposed class (3 points)
* __Part C: 2 points__
    * Follows project structure, submission, and formatting guidelines (1 point)
    * All functions (except main) have doc strings (see formatting guidelines for format) (1 point)


### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:
* Work with a basic class structure
* Develop your models for your final project

***

## Part A: Surfaces

For Part A of the lab this week, you will need to define two classes, Surface and Rectangle. These classes will represent an object’s appearance and location in space, respectively. We will also use a concept called composition to build the surface object. The classes are described below:

### Rectangle Class

In a file called `Rectangle.py`, define a class called `Rectangle`. The class should have the following interface:
* Instance Variables (i.e. attributes)
   * `self.x`
      * the x coordinate of its upper left position
   * `self.y`
      * the y coordinate of its upper left position
   * `self.height`
      * the height of the rectangle
   * `self.width`
      * The width of the rectangle
* Methods (i.e. behaviors)
    * `__init__(self, x, y, h, w)`
        * Takes x, y coordinates, as well as a width and height, and saves them as instance variables
    * `__str__(self)`
        * returns a string containing the x, y, width, and height of the rectangle.
            * For example: “(x : 5, y: 7) width: 10, height: 10”, where the integers are the values of the instance variables

### Surface Class

In a file called `Surface.py`, define a class called `Surface`. The class should have the following interface:
* Instance Variables (i.e. attributes)
   * `self.rect`
      * a rectangle object
   * `self.image`
      * the string containing the image file name
* Methods (i.e. behaviors)
   * `__init__(self, filename, x, y, h, w)`
      * Takes the filename string as a parameter and saves it to the `self.image` instance variable.
      * Also, takes a x, y set of coordinates, as well as a width and height, and creates a rectangle object stored in `self.rect`
   * `getRect(self)`
      * returns the rectangle object

:bulb: You will need to import your rectangle module into your `Surface.py` file to use the Rectangle class.

### Main Driver

Lastly, you should write a driver (main function) in a separate `lab8.py` file that imports both your `Surface` and `Rectangle` module. Your driver code will:
* create a surface object using whatever parameters you choose.
* call the getRect() method on the surface object, and save the result rectangle in a variable.
* call print on the resulting rectangle (which should automatically call the `__str__` function)
   * DO NOT call the `__str__` function explicitly

__Show your TA your code. If you were not able to finish, show the TA what you have completed.__

__--END OF IN LAB REQUIRED WORK. --__

__You may continue to work on the remainder of the lab on your own time or in lab__

## Part B: Testing your code

Each class is a model of some real world object. We often refer to data classes as the models in a GUI program. Your models show the logical structure of your application data, including the relationships and constraints that determine how data can be stored and accessed. Each model is represented by a class that you can instantiate (create new objects). In this lab you will design the data models for your final project. Your data models must not have any GUI components in them beyond positioning and image data. They only represent the state of the data you will need to represent in your GUI.

For example, if you are creating a space invaders type of game, you would need a class to represent the bullet, which could contain the image filename (str), the image and location of the bullet (represented by your Surface class from above), etc. The ship class would contain similar data values, along with methods such as moveLeft() and moveRight(), which would only update the ship coordinates.

Determine the interface (attributes and behaviors) your classes will need will need to define your data models, and update your proposal document to reflect your new class structure. As you work on your project you may find that you need to tweak your data models or even add new ones, and that’s okay. However, you will need a solid starting point to move forward, and that’s what you are doing here.

### Unit Testing

In a separate file, called `tests.py`, write a main driver that will test your classes. It is useful to write this file before writing your models to help you understand your design. This way you can test your code as you write it. It is also important that you write your test.py as clearly as possible, and try to anticipate the interface for your classes. You will need to constantly update this test file as you work on the models. This will become part of your final project validation testing.

Python has a special statement for testing code called assert.  The ‘assert’ statement test a boolean expression, and if the expression fails, ends the program. For example:

```python
assert True #no problem
assert False
    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    AssertionError
```

You must come up with your own tests that validate your code by verifying the validity of each method of each class. For example, for the previously stated ship’s moveRight() method, you should have something like the following:

```python
def main():
        print(“######## Testing ship model#########”)
        test_ship = ship.Ship();

        print(“=====Standard Input Test=====”)
        test_ship.moveRight(5)
        assert  test_ship.getCoordinates() == (5, 0)
        print(“=====Zero Input Test=====”)
        test_ship.moveRight(0)
        assert  test_ship.getCoordinates() == (5, 0)
        print(“=====Negative Input Test=====”)
        test_ship.moveRight(-1)
        assert  test_ship.getCoordinates() == (4, 0)
        #additional code...
main()

```

You will not yet be able to run this code because you haven’t written your models. The TA’s will check your test code next lab, and make suggestions regarding additional test or tweaks to your model interfaces.

## Part C: Submission
* Required code organization:
    * lab8.py
    * Rectangle.py
    * Surface.py

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
