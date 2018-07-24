import turtle

class LSystem:
	def __init__(self,file):
		""" instantiates the LSystem object by reading from a text file. Will print errors if the file is not found or if the formatting is incorrect.

		    args: self [LSystem] - the object that is being instantiated.
			  file [str] - a string representing the file to be opened.

		    return: None
		"""
		try:
			self.file = open(file,"r")
			self.angle = int(self.file.readline())
			self.iterations = int(self.file.readline())
			self.axiom = self.file.readline()
			self.rules = {}
			#strips the remaining lines and formats them into a rules dictionary
			for line in self.file:
				line = line.replace(" ","")
				line = line.replace("\n","")
				for i in range(len(line)):
					if line[i] == ":":
						self.rules[line[:i]] = line[i+1:]
			self.file.close()
		except TypeError:
			print("Error: file formatting is incorrect.")
		except:
			print("Error: file not found.")			

	def applyRules(self,char):
		""" checks if a character is in the rules dictionary and returns the rule if it is.

		    args: self [LSystem] - the object who's rules attribute is being accessed.
			  char [str] - the object that is checked to be a key to the rules dictionary.

		    return: char, if it is not a key to a dictionary.
			    the string corresponding to the char key in the rules dictionary.
		"""
		if self.rules.get(char):
			return self.rules[char]
		else:
			return char

	def processString(self):
		""" Converts each character in the LSystem's axiom to either itself or a rule corresponding to that string.

		    args: self [LSystem] - the object who's axiom is being accessed.

		    return: output - a new string to replace the axiom.
		"""
		output = ''
		for char in self.axiom:
			output += self.applyRules(char)
		return output

	def createLSystem(self):
		""" Takes the axiom of an LSystem and iterates n times returning a completed LSystem.

		    args: self [LSystem] - changes the axiom of the LSystem according to the rules.

		    return: None
		"""
		for i in range(self.iterations):
			self.axiom = self.processString()

	def drawLSystem(self,tortle):
		""" Directs a turtle object according to the LSystem's axiom.

		    args: self [LSystem] - the object who's axiom is being accessed to direct the turtle object.
			  tortle [Turtle] - the object being directed by the instructions from the axiom.

		    return: None
		"""
		distance = 10
		for i in self.axiom:
			if i == 'F':
				tortle.forward(distance)
			if i == '+':
				tortle.left(self.angle)
			if i == '-':
				tortle.right(self.angle)
