
import math
import turtle

def setUpWindow(screenObject):
	screenObject.setworldcoordinates(-360, -2, 360, 2)
	screenObject.bgcolor('navy')

def setUpTrutle(turtleObject):
	turtleObject.color('white')
	turtleObject.speed(0)
	turtleObject.goto(0,-365)
	turtleObject.goto(0,365)
	turtleObject.goto(0,0)
	turtleObject.goto(365,0)
	turtleObject.goto(-365,0)
	turtleObject.pendown()

def drawSineCurve(turtleObject):
	for i in range (-360,361):
		turtleObject.goto(i, math.sin(math.radians(i)))

def drawCosineCurve(turtleObject):
	turtleObject.penup()
	turtleObject.goto(-360,1)
	turtleObject.pendown()
	for i in range (-360,361):
		turtleObject.goto(i, math.cos(math.radians(i)))

def main():
	
	wn = turtle.Screen()
	fred = turtle.Turtle()

	setUpWindow(wn)
	setUpTrutle(fred)
	drawSineCurve(fred)
	drawCosineCurve(fred)
	
	wn.exitonclick()
main()
