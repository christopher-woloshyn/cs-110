import turtle

def applyRules(char,rules):
	if rules.get(char):
		return rules[char]
	else:
		return char

def processString(axiom,rules):
	output = ''
	for i in axiom:
		output += applyRules(i,rules)
	return output

def createLSystem(iterations,axiom,rules):
	for i in range(iterations):
		axiom = processString(axiom,rules)
	return axiom

def drawLSystem(orders,distance,degree):
	win = turtle.Screen()
	todd = turtle.Turtle()

	for i in orders:
		if i == 'F':
			todd.forward(distance)
			changeThickness(todd)
		if i == '+':
			todd.left(degree)
			changeColor(todd)
		if i == '-':
			todd.right(degree)
			changeColor(todd)
		if i == '[':
			x = todd.xcor()
			y = todd.ycor()
		if i == ']':
			todd.goto(x,y)

def changeColor(tortle):
	theta = tortle.heading() 
	inc_value = (theta % 60)/60
	dec_value = 1.0 - inc_value
	if theta < 60:
		tortle.pencolor((1.0,inc_value,0))
	elif theta < 120:
		tortle.pencolor((dec_value,1.0,0))
	elif theta < 180:
		tortle.pencolor((0,1.0,inc_value))
	elif theta < 240:
		tortle.pencolor((0,dec_value,1.0))
	elif theta < 300:
		tortle.pencolor((inc_value,0,1.0))
	elif theta < 360:
		tortle.pencolor((1.0,0,dec_value))

def changeThickness(tortle):
	d = tortle.distance(0,0)//20
	tortle.width(d)
