class MinStack:
	def __init__(self):
		self.stack , self.output = [] , []
		 
	def push(self, val):
		self.stack += [val]
		if self.output: self.output += [min(val, self.output[-1])]
		else: self.output += [val]
  
	def pop(self):
		self.stack = self.stack[:-1]
		self.output = self.output[:-1]
	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.output[-1]