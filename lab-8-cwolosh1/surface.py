import rectangle

class surface:
	def __init__(self,filename,x,y,h,w):
		self.rect = rectangle.rectangle(x,y,h,w)
		self.image = filename

	def getRect(self):
		return self.rect
