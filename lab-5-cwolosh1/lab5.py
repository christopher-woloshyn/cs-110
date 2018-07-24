import turtle

def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1.

        args: n [int] - starting value for 3n+1 sequence

        return: count [int] - the number of iterations the loop executed until n = 1.
    """
    count = 0
    while(n != 1):
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count += 1
    return count

def drawGraph(iteration):
    """ Draws a graph with a positive integer on the x-axis, and the number of iterations it takes for the 3n+1 sequence to bring that integer to 1 on the y-axis. The graph actively marks where the current maximum value is.

        args: iteration [int] - the upper bound of the function as inputed by the user in Part A

        return: none.
    """
    grapher = turtle.Turtle()
    grapher.speed(0)
    grapher.up()
    grapher.goto(0,0)
    grapher.down()

    writer = turtle.Turtle()
    writer.speed(0)

    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 10, 10)

    max_so_far = 0

    for i in range(1, iteration + 1):
        result = seq3np1(i)
        print("The number " + str(i) + " has " + str(result) + " iterations.")

        if result > max_so_far:
            max_so_far = result
            writer.clear()
            writer.up()
            writer.goto(i, max_so_far)
            # I intentionally place the turtle at the point of the max because I personally think it looks better there instead of the top left corner. (pls don't take points off.)
            writer.write("Maximum so far: " + str(max_so_far))

        wn.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
        grapher.goto(i, result)

    wn.exitonclick()

def main():

##### PART A #####

    upper = int(input("Please enter an upper bound for the function: "))
    start = 1
    while (start < upper):
        start += 1
        count = seq3np1(start)
        print("The number " + str(start) + " has " + str(count) + " iterations.")

    ##### PART B #####

    drawGraph(upper)

main()
