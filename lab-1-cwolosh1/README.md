#### CS 110 - Spring 2018
# Lab 1 - Getting Familiar with Your Environment
## Due Date: 5:00 p.m., January 25th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab1.py

### Grading Rubric

**_TOTAL: 10 points_**
* **Part B: 8 points**
    * Code runs as expected
* **Part C: 2 points**
    * Follows requested project structure and submission format
    * Follows [formatting guidelines](https://docs.google.com/document/d/1RU9bHsJhc4wecOXelXF5uUjcNTce4f2I0-09kJKvRvk/edit?usp=sharing)

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

## Part A: Learning the Environment and Writing the code

Part A must be completed in lab. Each lab during the semester will have a Part A that you must attempt to complete in lab. As soon as you complete Part A, you may show the TA and leave. If you cannot complete Part A by the end of lab, speak with the TA at the end of lab.

If you miss your lab time without prior arrangements with me or the TA, you cannot make up or complete part A outside of lab. In this case, you will not receive credit for Part A, even if completed (_many labs will require you to complete Part A in order to complete the lab_).

There will usually be additional parts to the lab that may be completed outside of lab on your own time.

_In this lab, you will learn to_:

* Use the command line to issue commands to the operating system
* Write and execute a simple python program in a command-line environment
* Use `git` to manage your projects and submit your work for grading.

Look for these icons!

| | Meaning |
|:----:|---------|
| :bulb: | Tips and useful information |
| :warning: | Caution! This could cause you problems. |
| :no_entry_sign: | Danger! Don't do this! |

Log into a machine using your PODS user id and password. (If you're reading this online in the lab, you've probably succeeded in doing this already.) Locate and launch a "terminal". We will call this, inter-changeably, a **terminal**, **shell**, or **command line**. The shell will accept and execute Linux commands, of which there are hundreds. We'll learn a few today, and I'll try to introduce you to more and more throughout the semester. You will need to get used to using the terminal, so don’t be afraid of it. You can’t ‘hurt’ the computer from the terminal.

The Linux help system is accessible through the system man pages. This is standard on all Unix/Linux distributions. "man" is short for "manual" (but the command is "man"). To access the man pages for a particular command, at the command prompt type the command "man" (without quotes) followed by the command you are interested in, followed by the <ENTER> key.
* :bulb: The basic format of entering commands in the terminal is:
    * *command* -*options* *args*
        * *command* : starts a program, just like clicking on an icon in the windowed environment
        * *option* : optional configuration flags that change the way the program runs. Usually preceded by a dash, -.
        * *args* : arguments the program needs to run, such as a key or filename
* For example, to read about the "pwd" command, type ‘man pwd’
    * This will open up the man program and display the help information for the pwd command. In the man page environment, to go forward and look at additional information that does not fit on the first screen, press the **ENTER** key.
* To exit the man page program, type the letter *q*.
* We will be using the following commands often, so review them in the man pages:
    * man
    * pwd
    * mkdir
    * rm
    * cd
    * ls
    * mv
    * cp
    * python3
* :warning: *These are Linux specific commands. Although some commands are similar on the windows console, most will not work the same or at all.*

### Using Linux Commands

Next, you will begin running and using some of the commands you learned about in the previous section above. In particular, complete the following steps:
* On the command line, type: cd ~
    * This takes you to your home directory if you are not already there.
    * :bulb: The ~ is just a shortcut symbol that means home directory
* Create a directory named cs110. On the command line, you can do this with the following command:
    * mkdir cs110
* Change your "current working directory" to be the cs110 directory. To do this, execute the following command:
    * cd cs110
* Confirm that you are in fact in the cs110 directory by typing the command:
    * pwd
* Type the command ‘python3’ to enter the Python Interactive Shell
    * Note the prompt (**<<<**) followed by your cursor (**|**)
    * This lets you know that you are in the Python shell, and that the interpreter is awaiting your input.
        * :warning: **The python shell is different from the linux terminal.** Think of it as a special python shell inside the linux shell.
    * Exit the shell with the *exit()* command
* The shell environment is the place where you should try out various Python expressions and statements,
    * :no_entry_sign: HOWEVER, it is NOT the proper environment in which to write an entire program
* In your interactive book, you can use the in-browser environment to write "snippets" of code, or Python scripts
    * :warning: These are NOT complete programs
* :bulb: In our class:
    * Complete programs will always be written in Python scripts
    * Complete programs will have a **main()** function
    * Complete programs will include an invocation of the **main()** function
    * Each complete program will be saved in a separate file given a **camelCaseName** followed by a **.py** extension (e.g., **computeAverageProfit.py**)
    * :no_entry_sign: *Note that file names should NEVER contain spaces*

## Part B: Writing the Code
The first thing we are going to do is initialize our folder to work with github.
First, let's set up our git credentials. Enter the following two commands in the terminal:

`git config --global user.name "Firstname Lastname"`

`git config --global user.email "email@binghamton.edu"`

You should be in your cs110 directory. If you are not, go back to part A and try to figure out how to get there. If you need help, ask a TA.

In this directory, you are going to clone this repository to get a copy of the source code onto your account. To do this, you will first need to have signed up for a Github account if you didn't already have one.

:bulb: If you don't have an account, ask the TA to help you.

Look at the Github landing page for your fork of this project. You should see a green button that says "Clone or download". Press it and you should see a URL like https://github.com/binghamtonuniversity-cs110/lab-1-username.git. Copy that text somewhere you can access it, then go back to the terminal.

Next, be sure you are still in the cs110 directory and execute the following command in the terminal:

`git clone URL`

:bulb: *where URL is the copied text ending in ".git".*

We will explore git workflows in-depth later in this lab.

Now that we have our repository set up, we will edit the code. Change your directory to the cloned repository. If you aren't sure how to do this, first review part A, and try to figure it out. As a last resort, ask the TA for help.

If you are not already familiar with a linux editor, please use gedit, which has several nice features for Python code development.

:warning: Beware that gedit is a linux editor, and will not work on other OS's.

You can use gedit to open a file by typing, for example, the following into a linux command shell:

`gedit lab1.py &`

If there is no file in the current folder named *lab1.py*, then gedit will create a new empty one for you (remember, you can check your current folder location with `pwd`). If the file does exist, it will edit the existing file.

:bulb: The ampersand at the end of the command says to run this application in the background. This will allows you to write some code, save it, then run it in the shell without quitting gedit.

After making changes to a file, you can save it by clicking "Save" at the top of the gedit window, or with the hot key command `<ctrl-s>`. Note that if you have made changes to an open file, and those changes have not been saved, the file name across the top of the window will be preceded by an asterisk (for example, "\*lab1.py"). To exit from gedit, make sure your modifications are saved, and then type `<ctrl-q>` in the gedit window, or simply close the gedit window by clicking the “x” in the upper right hand corner.

Open the accompanying *lab1.py* simple program with gedit. You must keep the format, indentation, and capitalization EXACTLY as it is!

* First run the program by typing the following command into the terminal: `python3 lab1.py`
* Next, using the code I have given you as an example, make the following additions to the code:
    * The **main()** function starts with the line `def main():`. After each variable assigned to inside the **main()** function, insert a print statement that prints both the value *and* the type of the variable
        * :bulb: You should use spaces, not tabs, to indent when writing your own code. Spaces are more cross platform compatible when switching between linux and Windows.
    * Ask the user to input how many times per week a class meets and save that in a variable called `classes_per_week`.
        * For example, our class meets 2 days a week
        * :warning: Don’t forget to convert the input from the user to an `int`. Notice that you have to convert all input from text to a number, as we did for the previous variables. Ensure you make this conversion by following the example from the previous code.
    * Calculate the cost per class by dividing the `cost_per_week` by the `classes_per_week` and save the result in a variable called `cost_per_class`
    * Print the `cost_per_class` to the console with a nice message
        * :bulb: try to figure out the syntax of this based on the syntax and behavior of the rest of your program
* Save your program, then run it and debug if necessary
    * If you have any difficulty completing this first assignment, ask your TA or post a note on Piazza to get help!

## Part C: Submission
* Required code naming and organization:
    * lab1.py

:no_entry: Every lab will have a required submission guidelines. Please read submission requirements carefully. Any deviations from specifications on future labs or projects will result in point deductions or incomplete grades.
### Git
In this and future labs, we will use Github Classroom repositories. You have already [forked](https://help.github.com/articles/fork-a-repo/) this repository when you accepted the emailed link. That makes a copy of the repository, free for you to make changes. Then you cloned your forked repository to get a working copy onto this machine.

Now that we have made local changes to our working copy, let's [commit](https://git-scm.com/docs/git-commit) those changes to the repository:

:warning: *These commands all presume that your current working directory is within the directory tracked by `git`.*

```shell
git commit -a -m "first commit"
```

The `-a` says that git should add all tracked files with changes to your commit, and the `-m` says the next string contains the commit message.

What about _untracked files_? Run the following commands:

```shell
echo $(whoami)@$(hostname):$(pwd) > information.txt
git status
```

You'll notice that `git` tells us that `information.txt` is an _untracked file_. That means it's not being tracked by the repository. Let's fix that by [adding](https://git-scm.com/docs/git-add) it.

```shell
git add information.txt
git commit -m "Added an informational file"
```

Once we've made the commits for a given coding session, we need to add those to the repository by performing a [push](https://git-scm.com/docs/git-push):

```shell
git push
```

Now, let's say we don't want `information.txt` in the repository anymore. How can we remove it?

```shell
git rm information.txt
git commit -m "Removed an informational file"
git push
```

Lastly, the next time we begin a coding session, we will need to [pull](https://git-scm.com/docs/git-pull) to get an updated working copy.

```shell
git pull
```

This will allow you to keep your code in the lab and on your own computer synchronized if you want to work outside of lab.

Lastly we are going to make our final commit. You will need to do this when your submission is ready for grading.

```shell
git commit --allow-empty -m "final commit"
git push
```

The `--allow-empty` option makes it possible to make a commit without having made any changes. This will enable you to just update the comment.

:bulb: You can commit as often as you like, and revert your code to any previous commit. I recommending making commits often with a comment describing the state of your code. The TAs will only grade your submission when the comment says "final commit".
:warning: You __MUST__ make a submission with the comment "final commit" before the deadline to be considered on time.

That's it! We've completed our work for this lab. We will use this submission process for all subsequent labs and assignments.

:bulb: Useful `git` references:
- https://guides.github.com/introduction/flow/
- https://help.github.com
- https://git-scm.com/doc
