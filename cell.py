class Cell:

	def __init__(self,i=0,j=0):
		self.g_val = 1000000
		self.f_val = 1000000
		self.search_val = 1000000
		self.x = i
		self.y = j
		self.status = 'x'
		self.parent = None

	def equals(self,second):
		if self.x == second.x and self.y == second.y:
			return True
		else:
			return False
