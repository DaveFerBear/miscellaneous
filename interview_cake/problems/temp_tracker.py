class TempTracker:
	def __init__(self):
		
		self.occurrences = [0] * (111)
		self.max_occurrences = 0
		self.mode = None

		self.sum = 0.0
		self.num = 0

		self.mean = None
		self.min = None
		self.max = None

	def insert(temp):
		self.max = max(self.max, temp)
		self.min = min(self.min, temp)
		
		self.num += 1
    self.sum += temperature
    self.mean = self.sum / self.num
		
    self.occurrences[temperature] += 1
		if self.occurrences[temperature] > self.max_occurrences:
    	self.mode = temperature
    	self.max_occurrences = self.occurrences[temperature]

	def max:
		return self.max

	def min:
		return self.min

	def mean:
		return self.mean

	def mode:
		return self.mode

